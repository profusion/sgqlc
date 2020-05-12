#!/usr/bin/env python3

'''
Agile Dashboard for a GitHub Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script will output a dashboard for GitHub issues and pull
requests of a repository.

It was the original tool that did lead to the development of
``sgqlc``, while the author was very familiar with GraphQL, using it
from Python was kind of painful.

:license: ISC
'''

__docformat__ = 'reStructuredText en'

import datetime
import json
import logging
import os
import re
import sys

from collections import OrderedDict

from sgqlc.operation import Operation  # noqa: I900
from sgqlc.endpoint.http import HTTPEndpoint  # noqa: I900
from github_schema import github_schema as schema  # noqa: I900

logger = logging.getLogger(__name__)


def json_pretty_print(d, file=None):
    args = {'sort_keys': True, 'indent': 2, 'separators': (',', ': ')}
    if file:
        return json.dump(d, file, **args)
    return json.dumps(d, **args)


def compact_fmt(d):
    s = []
    for k, v in d.items():
        if isinstance(v, dict):
            v = compact_fmt(v)
        elif isinstance(v, (list, tuple)):
            lst = []
            for e in v:
                if isinstance(e, dict):
                    lst.append(compact_fmt(e))
                else:
                    lst.append(repr(e))
            s.append('%s=[%s]' % (k, ', '.join(lst)))
            continue
        s.append('%s=%r' % (k, v))
    return '(' + ', '.join(s) + ')'


def report_download_errors(errors):
    logger.error('Document contain %d errors', len(errors))
    for i, e in enumerate(errors):
        msg = e.pop('message')
        extra = ''
        if e:
            extra = ' %s' % compact_fmt(e)
        logger.error('Error #%d: %s%s', i + 1, msg, extra)

    raise SystemExit('Failed to download')


def select_issues(repo, labels=(), states=(),
                  first=100, after=None, last=None, before=None):
    args = {}
    if labels:
        args['labels'] = labels
    if states:
        args['states'] = states
    if first:
        args['first'] = first
    if after:
        args['after'] = after
    if last:
        args['last'] = last
    if before:
        args['before'] = before

    conn = repo.issues(**args)
    conn.page_info.__fields__(
        has_next_page=True,
        end_cursor=True,
    )
    nodes = conn.nodes
    nodes.__fields__(
        number=True,
        state=True,
        title=True,
        body_text=True,
        created_at=True,
        closed_at=True,
    )
    nodes.labels(first=100).nodes.name()
    nodes.author.login()
    nodes.project_cards(first=100).nodes.project.id()
    nodes.milestone.id()
    nodes.assignees(first=100).nodes.login()


def select_pull_requests(repo, labels=(), states=(),
                         first=100, after=None, last=None, before=None):
    args = {}
    if labels:
        args['labels'] = labels
    if states:
        args['states'] = states
    if first:
        args['first'] = first
    if after:
        args['after'] = after
    if last:
        args['last'] = last
    if before:
        args['before'] = before

    conn = repo.pull_requests(**args)
    conn.page_info.__fields__(
        has_next_page=True,
        end_cursor=True,
    )
    nodes = conn.nodes
    nodes.__fields__(
        number=True,
        state=True,
        title=True,
        body_text=True,
        created_at=True,
        closed_at=True,
        merged_at=True,
        additions=True,
        deletions=True,
        head_ref_name=True,
    )
    nodes.labels(first=100).nodes.name()
    nodes.author.login()
    nodes.project_cards(first=100).nodes.project.id()
    nodes.milestone.id()
    nodes.assignees(first=100).nodes.login()

    reviews = nodes.reviews(first=100)
    reviews.nodes.author.login()
    reviews.nodes.__fields__(
        body_text=True,
        created_at=True,
        state=True,
    )


def create_operation(owner, name, labels=(), issue_states=(), pr_states=()):
    op = Operation(schema.Query)

    repo = op.repository(owner=owner, name=name)

    repo.labels(first=100).nodes.__fields__(
        name=True,
        color=True,
    )
    repo.milestones(first=100).nodes.__fields__(
        id=True,
        state=True,
        due_on=True,
        title=True,
        description=True,
    )
    repo.projects(first=100).nodes.__fields__(
        id=True,
        number=True,
        name=True,
        state=True,
    )
    select_issues(repo, labels, issue_states)
    select_pull_requests(repo, labels, pr_states)
    return op


def download(endpoint, reponame, labels=(), issue_states=(), pr_states=()):
    owner, name = reponame.split('/', 1)
    op = create_operation(owner, name, labels, issue_states, pr_states)

    logger.info('Downloading base information from %s', endpoint)
    logger.debug('Operation:\n%s', op)

    d = endpoint(op)
    errors = d.get('errors')
    if errors:
        return report_download_errors(errors)

    repodata = (op + d).repository
    while (repodata.issues.page_info.has_next_page
           or repodata.pull_requests.page_info.has_next_page):
        op = Operation(schema.Query)
        repo = op.repository(owner=owner, name=name)

        if repodata.issues.page_info.has_next_page:
            select_issues(
                repo, labels, issue_states,
                after=repodata.issues.page_info.end_cursor)

        if repodata.pull_requests.page_info.has_next_page:
            select_pull_requests(
                repo, labels, pr_states,
                after=repodata.pull_requests.page_info.end_cursor)

        logger.info(
            'Downloading extra connection nodes: issues=%s, prs=%s',
            repodata.issues.page_info, repodata.pull_requests.page_info)
        logger.debug('Operation:\n%s', op)

        cont = endpoint(op)
        errors = cont.get('errors')
        if errors:
            return report_download_errors(errors)

        contdata = (op + cont).repository
        if repodata.issues.page_info.has_next_page:
            repodata.issues += contdata.issues

        if repodata.pull_requests.page_info.has_next_page:
            repodata.pull_requests += contdata.pull_requests

    logger.info('Finished downloading repository: %s', reponame)
    logger.debug('%s', repodata)
    return d


class ComplexObjectFilter:
    '''Filter by number of string attribute, including regexp.

    Used to filter projects and milestones, this will check if the
    filter ``f`` is an integer and filter by property ``obj.number``,
    otherwise, if ``f`` is a string, will check if it matches
    ``attrname`` attribute of object. Last but not least it will call
    ``f.search()`` with attribute ``attrname`` of object, allowing a
    compiled regular expression to be used.
    '''
    def __init__(self, f, attrname):
        if isinstance(f, str):
            self.matches = lambda obj: getattr(obj, attrname) == f
        elif isinstance(f, int):
            self.matches = lambda obj: obj.number == f
        else:
            self.matches = lambda obj: bool(f.search(getattr(obj, attrname)))


class GitHubAgileDashboard:
    '''Base class for Agile Dashboard over GitHub database.

    Given a repository data structure ``repo`` which matches GitHub's
    GraphQL (API v4) schema, then extra filters are applied and the
    following members will be populated:

     - ``labels`` dict with keys being name
     - ``projects`` dict with keys being ``Node.id``
     - ``milestones`` dict with keys being ``Node.id``
     - ``issues`` dict with keys being ``Issue.number``
     - ``pull_requests`` dict with keys being ``PullRequest.number``

    The unfiltered versions are prefixed with ``all_``, ie:
    ``all_labels`` contains all labels in the repository.

    The following lists provide insights to render Agile Dashboards:

     - ``todo`` open and unassigned issues
     - ``working`` open and assigned issues
     - ``reviewing`` open pull requests
     - ``done`` closed or merged pull requests or issues

    Extra members that may be useful:

     - ``max_number`` the maximum ``Issue.number`` and
       ``PullRequest.number``, can be used to indentation/formatting
       purposes.

    '''
    def __init__(self, repo,
                 filter_labels=(),
                 filter_issue_states=(),
                 filter_pr_states=(),
                 filter_projects=(),
                 filter_milestones=(),
                 filter_assignees=()):
        self.repo = repo
        self.labels = {}
        self.projects = {}
        self.milestones = {}
        self.issues = {}
        self.pull_requests = {}

        self.all_labels = {}
        self.all_projects = {}
        self.all_milestones = {}
        self.all_issues = {}
        self.all_pull_requests = {}

        self.todo = []
        self.working = []
        self.reviewing = []
        self.done = []

        self.max_number = 0

        self.any_milestone = not bool(filter_milestones)
        self.any_project = not bool(filter_projects)

        self.filter_label = self._build_filter(filter_labels)
        self.filter_issue_state = self._build_filter(filter_issue_states)
        self.filter_pr_state = self._build_filter(filter_pr_states)
        self.filter_project = self._build_complex_filter(
            filter_projects, 'name')
        self.filter_milestone = self._build_complex_filter(
            filter_milestones, 'title')
        self.filter_assignee = self._build_filter(filter_assignees)

        self.populate()

    def populate(self):
        self.populate_labels()
        self.populate_projects()
        self.populate_milestones()
        self.populate_issues()
        self.populate_requests()

    def populate_labels(self):
        if self.repo.labels:
            for n in self.repo.labels.nodes:
                self.all_labels[n.name] = n
                if self.filter_label(n.name):
                    self.labels[n.name] = n

    def populate_projects(self):
        if self.repo.projects:
            for n in self.repo.projects.nodes:
                self.all_projects[n.id] = n
                if self.filter_project(n):
                    self.projects[n.id] = n

    def populate_milestones(self):
        if self.repo.milestones:
            for n in self.repo.milestones.nodes:
                self.all_milestones[n.id] = n
                if self.filter_milestone(n):
                    self.milestones[n.id] = n

    def populate_issues(self):
        if self.repo.issues:
            for n in self.repo.issues.nodes:
                self.all_issues[n.number] = n
                if self.filter_issue(n):
                    self.issues[n.number] = n
                    self.max_number = max(self.max_number, n.number)
                    if n.state == 'OPEN':
                        if not n.assignees or not n.assignees.nodes:
                            self.todo.append(n)
                        else:
                            self.working.append(n)
                    else:
                        self.done.append(n)

    def populate_requests(self):
        if self.repo.pull_requests:
            for n in self.repo.pull_requests.nodes:
                self.all_pull_requests[n.number] = n
                if self.filter_pull_request(n):
                    self.pull_requests[n.number] = n
                    self.max_number = max(self.max_number, n.number)
                    if n.state == 'OPEN':
                        self.reviewing.append(n)
                    else:
                        self.done.append(n)

    def filter_connection(self, conn, filter_cb, attrname):
        if not conn or not conn.nodes:
            return filter_cb(None)
        for n in conn.nodes:
            if filter_cb(getattr(n, attrname)):
                return True
        return False

    def filter_project_cards(self, obj):
        if not hasattr(obj, 'projects'):
            obj.projects = []
        if not obj.project_cards or not obj.project_cards.nodes:
            return self.any_project
        for n in obj.project_cards.nodes:
            if n.project.id in self.projects:
                n.project = self.projects[n.project.id]
                if n.project not in obj.projects:
                    obj.projects.append(n.project)
                return True
        return False

    def filter_milestone_id(self, obj):
        if not obj.milestone:
            return self.any_milestone
        if obj.milestone.id in self.milestones:
            obj.milestone = self.milestones[obj.milestone.id]
            return True
        return False

    def filter_common(self, node):
        if not self.filter_connection(
                node.labels, self.filter_label, 'name'):
            return False
        if not self.filter_project_cards(node):
            return False
        if not self.filter_milestone_id(node):
            return False
        if not self.filter_connection(
                node.assignees, self.filter_assignee, 'login'):
            return False
        return True

    def filter_issue(self, issue):
        if not self.filter_issue_state(issue.state):
            return False
        return self.filter_common(issue)

    def filter_pull_request(self, pr):
        if not self.filter_pr_state(pr.state):
            return False
        return self.filter_common(pr)

    @staticmethod
    def _build_filter(lst):
        if not lst:
            return lambda x: True
        return lambda x: x in lst

    @staticmethod
    def _build_complex_filter(lst, attrname):
        if not lst:
            return lambda x: True
        filters_lst = tuple(ComplexObjectFilter(e, attrname) for e in lst)
        return lambda x: any(f.matches(x) for f in filters_lst)


def cmd_save(endpoint, args):
    d = download(endpoint, args.repo,
                 args.label, args.issue_state, args.pr_state)
    if args.pretty:
        return json_pretty_print(d, args.file)
    return json.dump(d, args.file, sort_keys=True, separators=(',', ':'))


def create_complex_filter_list(lst):
    ret = []
    for e in lst:
        try:
            ret.append(int(e))
            continue
        except ValueError:
            pass

        if e.startswith('/') and e.endswith('/'):
            try:
                ret.append(re.compile(e[1:-1]))
                continue
            except re.error:
                pass

        ret.append(e)

    return tuple(ret)


def create_simple_filter_list(lst):
    ret = list(lst)
    if '' in ret:
        ret.remove('')
        ret.append(None)
    return tuple(ret)


def create_state_filter_list(lst):
    if lst == ['']:
        return (None,)  # won't match anything
    return tuple(lst)


def create_dashboard(endpoint, args):
    labels = create_simple_filter_list(args.label)
    issue_states = create_state_filter_list(args.issue_state)
    pr_states = create_state_filter_list(args.pr_state)
    projects = create_complex_filter_list(args.project)
    milestones = create_complex_filter_list(args.milestone)
    assignees = create_simple_filter_list(args.assignee)

    if args.load:
        try:
            d = json.load(args.load)
        except json.decoder.JSONDecodeError as exc:
            raise SystemExit('Failed to parse: %s' % (exc,)) from exc
        if d is None:
            raise SystemExit('Failed to load!')
    else:
        d = download(endpoint, args.repo, args.label,
                     args.issue_state, args.pr_state)

    op = create_operation(args.repo, args.label,
                          args.issue_state, args.pr_state)
    repodata = (op + d).repository
    return GitHubAgileDashboard(
        repodata, labels, issue_states, pr_states,
        projects, milestones, assignees,
    )


# TODO: refactor this into classes, is too complex (C901)
def cmd_dashboard_text(endpoint, args):  # noqa: C901
    dashboard = create_dashboard(endpoint, args)
    outfile = sys.stdout

    colors = {
        'Issue': {
            'state': {
                'OPEN': '\033[1;33m',
                'CLOSED': '\033[1;32m',
            },
        },
        'PullRequest': {
            'state': {
                'OPEN': '\033[1;33m',
                'MERGED': '\033[1;32m',
                'CLOSED': '\033[1;35m',
            },
            'unreviewed': '\033[1;33m',
            'reviews': {
                'APPROVED': '\033[1;32m',
                'CHANGES_REQUESTED': '\033[1;31m',
                'COMMENTED': '\033[1;37m',
                'DISMISSED': '\033[1;34m',
                'PENDING': '\033[1;33m',
            },
        },
        'todo': '\033[1;31m',
        'working': '\033[1;33m',
        'reviewing': '\033[1;36m',
        'done': '\033[1;32m',
        'clear': '\033[0m',
        'number': '\033[1m',
        'body': '\033[0m',
        'key-value': '\033[36m',
        'overtime': '\033[31m',
        'deadline': '\033[1;33m',
        'oneline': {
            'assignees': '\033[1;37m',
        },
    }

    def label_rgb_to_ansi_index(r, g, b, bright):
        return 'label-%d-%d-%d-%d' % (int(r), int(g), int(b), int(bright))

    colors[label_rgb_to_ansi_index(0, 0, 0, 0)] = '\033[0;97;40m'
    colors[label_rgb_to_ansi_index(1, 0, 0, 0)] = '\033[0;97;41m'
    colors[label_rgb_to_ansi_index(0, 1, 0, 0)] = '\033[0;97;42m'
    colors[label_rgb_to_ansi_index(1, 1, 0, 0)] = '\033[0;90;43m'
    colors[label_rgb_to_ansi_index(0, 0, 1, 0)] = '\033[0;97;44m'
    colors[label_rgb_to_ansi_index(1, 0, 1, 0)] = '\033[0;90;45m'
    colors[label_rgb_to_ansi_index(0, 1, 1, 0)] = '\033[0;90;46m'
    colors[label_rgb_to_ansi_index(1, 1, 1, 1)] = '\033[0;30;47m'

    colors[label_rgb_to_ansi_index(0, 0, 0, 1)] = '\033[0;97;100m'
    colors[label_rgb_to_ansi_index(1, 0, 0, 1)] = '\033[0;97;101m'
    colors[label_rgb_to_ansi_index(0, 1, 0, 1)] = '\033[0;97;102m'
    colors[label_rgb_to_ansi_index(1, 1, 0, 1)] = '\033[0;30;103m'
    colors[label_rgb_to_ansi_index(0, 0, 1, 1)] = '\033[0;97;104m'
    colors[label_rgb_to_ansi_index(1, 0, 1, 1)] = '\033[0;30;105m'
    colors[label_rgb_to_ansi_index(0, 1, 1, 1)] = '\033[0;30;106m'
    colors[label_rgb_to_ansi_index(1, 1, 1, 1)] = '\033[0;30;107m'

    no_colors = False
    if args.colors != 'yes' and (not outfile.isatty() or args.colors == 'no'):
        no_colors = True

        def uncolorize_dict(d):
            for k, v in tuple(d.items()):  # copy to modify d while iterating
                if isinstance(v, str):
                    d[k] = ''
                elif isinstance(v, dict):
                    uncolorize_dict(v)

        uncolorize_dict(colors)

    def out(color='', text='', end='\n'):
        outfile.writelines((color, text, colors['clear'], end))

    review_state_symbol = {
        'APPROVED': '+',
        'CHANGES_REQUESTED': '-',
        'COMMENTED': '"',
        'DISMISSED': '#',
        'PENDING': '?',
    }

    number_len = len(str(dashboard.max_number))
    number_fmt = '%%%dd' % number_len
    if args.format == 'oneline':
        title_len = os.environ.get('COLUMNS', 80) - number_len - 2

        def get_assignees(node):
            if not node.assignees or not node.assignees.nodes:
                return ''
            return '[' + ','.join(a.login for a in node.assignees.nodes) + '] '

        def out_common(node, title_len=title_len):
            color = colors[node.__class__.__name__]['state'][node.state]
            out(colors['number'], number_fmt % node.number, ' ')

            assignees = get_assignees(node)
            if assignees:
                out(colors['oneline']['assignees'], assignees, '')
                title_len -= len(assignees)

            out(color, node.title[:title_len], ' ')

        def out_issue(issue):
            out_common(issue)
            out()

        review_state_len = len(schema.PullRequestReviewState.__choices__)

        def get_reviews_summary(pr):
            if not pr.reviews or not pr.reviews.nodes:
                s = '!' * review_state_len
                return '%s%s' % (colors['PullRequest']['unreviewed'], s)

            final = set()
            for r in pr.reviews.nodes:
                final.add(r.state)

            def fmt_review_state(state):
                color = colors['PullRequest']['reviews'][state]
                sym = review_state_symbol[state]
                return '%s%s' % (color, sym)
            return ''.join(fmt_review_state(state) for state in final)

        def out_pr(pr):
            out_common(pr, title_len - review_state_len - 3)
            out('', ' [%s%s]' % (get_reviews_summary(pr), colors['clear']), '')
            out()

        def out_header(name, label):
            prefix = '-' * number_len
            text = ' %s: %d' % (label, len(getattr(dashboard, name)))
            out(colors[name], prefix + text)

    elif args.format in ('full', 'medium'):
        prefix = ' ' * number_len + ' '

        def out_key_val(key, value):
            if not value:
                return
            try:
                color = colors[key]
            except KeyError:
                color = colors['key-value']
            title = key.replace('_', ' ').title()
            out(color, '%s%s: %s' % (prefix, title, value))

        def get_labels(node):
            if not node.labels or not node.labels.nodes:
                return ''

            def fmt_label(n):
                if no_colors:
                    return n.name
                label = dashboard.all_labels.get(n.name)
                if not label:
                    return n.name
                color = label.color
                red = int(color[0:2], 16) >> 6
                green = int(color[2:4], 16) >> 6
                blue = int(color[4:6], 16) >> 6

                is_red = red > 0
                is_green = green > 0
                is_blue = blue > 0

                is_high_red = red > 1
                is_high_green = green > 1
                is_high_blue = blue > 1

                is_bright = is_high_red or is_high_green or is_high_blue
                if is_bright:
                    is_red = is_high_red
                    is_green = is_high_green
                    is_blue = is_high_blue

                color = colors[label_rgb_to_ansi_index(
                    is_red, is_green, is_blue, is_bright)]
                return '%s%s%s' % (color, n.name, colors['clear'])

            return ', '.join(fmt_label(n) for n in node.labels.nodes)

        today = datetime.datetime.now(datetime.timezone.utc)

        def get_milestone(node):
            if not node.milestone:
                return ''
            m = node.milestone

            color = ''
            if m.due_on < today:
                color = colors['overtime']
            else:
                td = m.due_on - today
                if td.days < 7:
                    color = colors['deadline']

            date = m.due_on.date().isoformat()
            return '%s %sdue %s' % (m.title, color, date)

        def get_projects(node):
            if not node.projects:
                return ''
            return ', '.join(p.name for p in node.projects)

        def get_assignees(node):
            if not node.assignees or not node.assignees.nodes:
                return ''
            return ', '.join(a.login for a in node.assignees.nodes)

        def out_common(node):
            color = colors[node.__class__.__name__]['state'][node.state]
            out(colors['number'], number_fmt % node.number, ' ')
            out(color, node.title)

            out_key_val('author', node.author.login)
            out_key_val('created_at', node.created_at)
            out_key_val('closed_at', node.closed_at)
            out_key_val('labels', get_labels(node))
            out_key_val('milestone', get_milestone(node))
            out_key_val('projects', get_projects(node))
            out_key_val('assigness', get_assignees(node))

        def out_body(node):
            body_color = colors['body']
            out()
            body_prefix = prefix + '  '
            for ln in node.body_text.splitlines():
                out(body_color, body_prefix + ln.rstrip())

        def out_issue(issue):
            out_common(issue)
            if args.format == 'full':
                out_body(issue)
            out()

        def get_reviews_summary(pr):
            if not pr.reviews or not pr.reviews.nodes:
                return '%sunreviewed' % (colors['PullRequest']['unreviewed'],)

            final = OrderedDict()
            for r in pr.reviews.nodes:
                final[r.author.login] = r

            def fmt_review(r):
                color = colors['PullRequest']['reviews'][r.state]
                sym = review_state_symbol[r.state]
                author = r.author.login
                return '%s%s%s%s' % (color, sym, author, colors['clear'])
            return ', '.join(fmt_review(r) for r in final.values())

        def out_pr(pr):
            out_common(pr)
            out_key_val('reviews', get_reviews_summary(pr))
            if args.format == 'full':
                out_body(issue)
                out_key_val('diff', '-%d/+%d' % (pr.deletions, pr.additions))
                out_key_val('ref', pr.head_ref_name)
                out_body(issue)
            out()

        def out_header(name, label):
            prefix = '-' * number_len
            text = ' %s: %d' % (label, len(getattr(dashboard, name)))
            out(colors[name], prefix + text)

    def out_node(node):
        if isinstance(node, schema.Issue):
            out_issue(node)
        else:
            out_pr(node)

    out_header('todo', 'To Do')
    for issue in dashboard.todo:
        out_issue(issue)

    out()
    out_header('working', 'Working')
    for issue in dashboard.working:
        out_issue(issue)

    out()
    out_header('reviewing', 'Reviewing')
    for pr in dashboard.reviewing:
        out_pr(pr)

    out()
    out_header('done', 'Done')
    for node in dashboard.done:
        out_node(node)


DEFAULT_GRAPHQL_ENDPOINT = 'https://api.github.com/graphql'

if __name__ == '__main__':
    import argparse
    import configparser
    import os.path

    cfg_path = os.path.expanduser('~/.github-agile-dashboard.cfg')

    cp = configparser.ConfigParser()
    cp['github-agile-dashboard'] = {
        'token': '',
        'graphql-endpoint': DEFAULT_GRAPHQL_ENDPOINT,
    }
    cp.read(cfg_path)
    cfg = cp['github-agile-dashboard']

    ap = argparse.ArgumentParser(description='GitHub Agile Dashboard')

    def tuple_arg(s):
        return s.split('=', 1)

    # Generic options to access the GraphQL API
    ap.add_argument('--graphql-endpoint',
                    help=('GitHub GraphQL endpoint. '
                          'May be stored in "' + cfg_path + '", section: '
                          '[github-agile-dashboard], key: '
                          'graphql-endpoint=URL. '
                          'Default=%(default)s'),
                    default=DEFAULT_GRAPHQL_ENDPOINT)
    ap.add_argument('--token', '-T',
                    help=('API token to use. '
                          'May be stored in "' + cfg_path + '", section: '
                          '[github-agile-dashboard], key: '
                          'token=STRING'))
    ap.add_argument('--verbose', '-v',
                    help='Increase verbosity',
                    action='count',
                    default=0)
    ap.add_argument('--label', '-l', action='append',
                    help='Filter issues and PR by label.',
                    default=[])
    ap.add_argument('--issue-state', action='append',
                    help=('Filter Issues by state. '
                          'Providing a single empty string disables Issues'),
                    choices=schema.IssueState.__choices__ + ('',),
                    default=[])
    ap.add_argument('--pr-state', action='append',
                    help=('Filter Pull Requests by state. '
                          'Providing a single empty string disables '
                          'Pull Requests'),
                    choices=schema.PullRequestState.__choices__ + ('',),
                    default=[])
    ap.add_argument('repo',
                    help='Repository name, such as "team/repo".')

    subparsers = ap.add_subparsers(dest='command')

    # Save GraphQL to JSON
    sp = subparsers.add_parser('save', help='Download and save JSON to disk')
    sp.set_defaults(func=cmd_save)
    sp.add_argument('--pretty', '-p', action='store_true',
                    help='Pretty print JSON')
    sp.add_argument('file', type=argparse.FileType('w'), nargs='?',
                    help='Where to save the JSON payload',
                    default=sys.stdout)

    # Dashboard for a Milestone
    sp = subparsers.add_parser('dashboard',
                               help='View Agile Dashboard as text output')
    sp.set_defaults(func=cmd_dashboard_text)
    sp.add_argument('--load', type=argparse.FileType('r'),
                    help='Where to load saved JSON, otherwise downloads.')
    sp.add_argument('--project', '-p', action='append',
                    help=('Filter issues and PR by project title or number. '
                          'If a string and starts and ends with "/", '
                          'will be handled as regular expression, '
                          'ie: "/^prefix-/".'),
                    default=[])
    sp.add_argument('--milestone', '-m', action='append',
                    help=('Filter issues and PR by milestone title or number. '
                          'If a string and starts and ends with "/", '
                          'will be handled as regular expression, '
                          'ie: "/^prefix-/".'),
                    default=[])
    sp.add_argument('--assignee', '-a', action='append',
                    help=('Filter issues and PR by assignees. '
                          'Use empty assignee to state "unassigned"'),
                    default=[])
    sp.add_argument('--colors', '-C', choices=('auto', 'yes', 'no'),
                    help=('Select color mode (ansi colors for terminals)'),
                    default='auto')
    sp.add_argument('--format', '-f', choices=('oneline', 'medium', 'full'),
                    help=('How to format issues and pull requests'),
                    default='oneline')

    args = ap.parse_args()

    endpoint_loglevel = max(10, 40 - ((args.verbose - 3) * 10))
    logfmt = '%(levelname)s: %(message)s'
    if endpoint_loglevel < logging.ERROR:
        logfmt = '%(levelname)s:%(name)s: %(message)s'

    logging.basicConfig(format=logfmt, level=max(10, 40 - (args.verbose * 10)))
    HTTPEndpoint.logger.setLevel(endpoint_loglevel)

    graphql_endpoint = (args.graphql_endpoint or cfg['graphql-endpoint']
                        or DEFAULT_GRAPHQL_ENDPOINT)
    token = args.token or cfg['token']
    if not token:
        raise SystemExit('token must be provided. You may create an '
                         'app or personal token at '
                         'https://github.com/settings/tokens')
    endpoint = HTTPEndpoint(graphql_endpoint, {
        'Authorization': 'bearer ' + token,
    })

    if not args.command:
        raise SystemExit('missing subcommand. See --help.')
    args.func(endpoint, args)
