import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


github_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
github_schema -= sgqlc.types.relay.Node
github_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

String = sgqlc.types.String

ID = sgqlc.types.ID

class URI(sgqlc.types.Scalar):
    __schema__ = github_schema


Int = sgqlc.types.Int

DateTime = sgqlc.types.datetime.DateTime

class ProjectState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class HTML(sgqlc.types.Scalar):
    __schema__ = github_schema


class ProjectCardState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CONTENT_ONLY', 'NOTE_ONLY', 'REDACTED')


class CommentAuthorAssociation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MEMBER', 'OWNER', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE')


class CommentCannotUpdateReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INSUFFICIENT_ACCESS', 'LOCKED', 'LOGIN_REQUIRED', 'MAINTENANCE', 'VERIFIED_EMAIL_REQUIRED')


class IssueOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'COMMENTS')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ASC', 'DESC')


class IssueState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class LockReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OFF_TOPIC', 'TOO_HEATED', 'RESOLVED', 'SPAM')


class ReactionContent(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('THUMBS_UP', 'THUMBS_DOWN', 'LAUGH', 'HOORAY', 'CONFUSED', 'HEART')


class ReactionOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class SubscriptionState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UNSUBSCRIBED', 'SUBSCRIBED', 'IGNORED', 'UNAVAILABLE')


class GitObjectID(sgqlc.types.Scalar):
    __schema__ = github_schema


class GitTimestamp(sgqlc.types.Scalar):
    __schema__ = github_schema


class GitSignatureState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('VALID', 'INVALID', 'MALFORMED_SIG', 'UNKNOWN_KEY', 'BAD_EMAIL', 'UNVERIFIED_EMAIL', 'NO_USER', 'UNKNOWN_SIG_TYPE', 'UNSIGNED', 'GPGVERIFY_UNAVAILABLE', 'GPGVERIFY_ERROR', 'NOT_SIGNING_KEY', 'EXPIRED_KEY')


class StatusState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('EXPECTED', 'ERROR', 'FAILURE', 'PENDING', 'SUCCESS')


class PullRequestState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED', 'MERGED')


class RepositoryPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLIC', 'PRIVATE')


class RepositoryOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT', 'NAME', 'STARGAZERS')


class RepositoryAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OWNER', 'COLLABORATOR', 'ORGANIZATION_MEMBER')


class MilestoneState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class MergeableState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MERGEABLE', 'CONFLICTING', 'UNKNOWN')


class IssuePubSubTopic(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED', 'MARKASREAD')


class PullRequestReviewState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'COMMENTED', 'APPROVED', 'CHANGES_REQUESTED', 'DISMISSED')


class PullRequestPubSubTopic(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED', 'MARKASREAD', 'HEAD_REF')


class TeamPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SECRET', 'VISIBLE')


class TeamMemberRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MAINTAINER', 'MEMBER')


class TeamMembershipType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('IMMEDIATE', 'CHILD_TEAM', 'ALL')


class RepositoryPermission(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ADMIN', 'WRITE', 'READ')


class TeamRepositoryOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT', 'NAME', 'PERMISSION', 'STARGAZERS')


class ProjectOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'NAME')


Float = sgqlc.types.Float

Date = sgqlc.types.datetime.Date

class X509Certificate(sgqlc.types.Scalar):
    __schema__ = github_schema


class DefaultRepositoryPermissionField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('READ', 'WRITE', 'ADMIN')


class TeamRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ADMIN', 'MEMBER')


class TeamOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NAME',)


class StarOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('STARRED_AT',)


class GistPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLIC', 'SECRET', 'ALL')


class GistOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT')


class OrganizationInvitationType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('USER', 'EMAIL')


class OrganizationInvitationRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DIRECT_MEMBER', 'ADMIN', 'BILLING_MANAGER', 'REINSTATE')


class DeploymentStatusState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'SUCCESS', 'FAILURE', 'INACTIVE', 'ERROR')


class DeploymentState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ABANDONED', 'ACTIVE', 'DESTROYED', 'ERROR', 'FAILURE', 'INACTIVE', 'PENDING')


class RepositoryLockReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MOVING', 'BILLING', 'RENAME', 'MIGRATING')


class RepositoryCollaboratorAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ALL', 'OUTSIDE')


class CollaboratorAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OUTSIDE', 'DIRECT', 'ALL')


class LanguageOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SIZE',)


class RefOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TAG_COMMIT_DATE', 'ALPHABETICAL')


class ReleaseOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'NAME')


class GitSSHRemote(sgqlc.types.Scalar):
    __schema__ = github_schema


class RepositoryContributionType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('COMMIT', 'ISSUE', 'PULL_REQUEST', 'REPOSITORY', 'PULL_REQUEST_REVIEW')


class SearchType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ISSUE', 'REPOSITORY', 'USER')


class PullRequestReviewEvent(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('COMMENT', 'APPROVE', 'REQUEST_CHANGES', 'DISMISS')


class TopicSuggestionDeclineReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NOT_RELEVANT', 'TOO_SPECIFIC', 'PERSONAL_PREFERENCE', 'TOO_GENERAL')



########################################################################
# Input Objects
########################################################################
class IssueOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ReactionOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ReactionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class CommitAuthor(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(ID, graphql_name='id')
    emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='emails')


class RepositoryOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamRepositoryOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ProjectOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class StarOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(StarOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class GistOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(GistOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LanguageOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(LanguageOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RefOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(RefOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ReleaseOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ReleaseOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class AddReactionInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')


class RemoveReactionInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')


class UpdateSubscriptionInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subscribable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subscribableId')
    state = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='state')


class AddCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class CreateProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')


class UpdateProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    state = sgqlc.types.Field(ProjectState, graphql_name='state')
    public = sgqlc.types.Field(Boolean, graphql_name='public')


class DeleteProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')


class AddProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class MoveProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_column_id = sgqlc.types.Field(ID, graphql_name='afterColumnId')


class UpdateProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DeleteProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')


class AddProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    note = sgqlc.types.Field(String, graphql_name='note')


class UpdateProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectCardId')
    note = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='note')


class MoveProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_card_id = sgqlc.types.Field(ID, graphql_name='afterCardId')


class DeleteProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')


class LockLockableInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    lockable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lockableId')
    lock_reason = sgqlc.types.Field(LockReason, graphql_name='lockReason')


class AddPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(String, graphql_name='body')
    event = sgqlc.types.Field(PullRequestReviewEvent, graphql_name='event')
    comments = sgqlc.types.Field(sgqlc.types.list_of('DraftPullRequestReviewComment'), graphql_name='comments')


class DraftPullRequestReviewComment(sgqlc.types.Input):
    __schema__ = github_schema
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class SubmitPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    event = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewEvent), graphql_name='event')
    body = sgqlc.types.Field(String, graphql_name='body')


class UpdatePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class DismissPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')


class DeletePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')


class AddPullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    in_reply_to = sgqlc.types.Field(ID, graphql_name='inReplyTo')


class UpdatePullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewCommentId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class RemoveOutsideCollaboratorInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')


class RequestReviewsInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='userIds')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='teamIds')
    union = sgqlc.types.Field(Boolean, graphql_name='union')


class AddStarInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')


class RemoveStarInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')


class AcceptTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DeclineTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    reason = sgqlc.types.Field(sgqlc.types.non_null(TopicSuggestionDeclineReason), graphql_name='reason')


class UpdateTopicsInput(sgqlc.types.Input):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    topic_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topicNames')



########################################################################
# Output Objects and Interfaces
########################################################################
class Query(sgqlc.types.Type):
    __schema__ = github_schema
    code_of_conduct = sgqlc.types.Field('CodeOfConduct', graphql_name='codeOfConduct', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    codes_of_conduct = sgqlc.types.Field(sgqlc.types.list_of('CodeOfConduct'), graphql_name='codesOfConduct')
    license = sgqlc.types.Field('License', graphql_name='license', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    licenses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('License')), graphql_name='licenses')
    marketplace_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketplaceCategory'))), graphql_name='marketplaceCategories', args=sgqlc.types.ArgDict((
        ('exclude_empty', sgqlc.types.Arg(Boolean, graphql_name='excludeEmpty', default=None)),
))
    )
    marketplace_category = sgqlc.types.Field('MarketplaceCategory', graphql_name='marketplaceCategory', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    marketplace_listing = sgqlc.types.Field('MarketplaceListing', graphql_name='marketplaceListing', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    marketplace_listings = sgqlc.types.Field(sgqlc.types.non_null('MarketplaceListingConnection'), graphql_name='marketplaceListings', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('category_slug', sgqlc.types.Arg(String, graphql_name='categorySlug', default=None)),
        ('viewer_can_admin', sgqlc.types.Arg(Boolean, graphql_name='viewerCanAdmin', default=None)),
        ('admin_id', sgqlc.types.Arg(ID, graphql_name='adminId', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationId', default=None)),
        ('all_states', sgqlc.types.Arg(Boolean, graphql_name='allStates', default=None)),
        ('slugs', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='slugs', default=None)),
        ('primary_category_only', sgqlc.types.Arg(Boolean, graphql_name='primaryCategoryOnly', default=Boolean(False))),
        ('with_free_trials_only', sgqlc.types.Arg(Boolean, graphql_name='withFreeTrialsOnly', default=Boolean(False))),
))
    )
    meta = sgqlc.types.Field(sgqlc.types.non_null('GitHubMetadata'), graphql_name='meta')
    node = sgqlc.types.Field('Node', graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Node')), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    organization = sgqlc.types.Field('Organization', graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    rate_limit = sgqlc.types.Field('RateLimit', graphql_name='rateLimit', args=sgqlc.types.ArgDict((
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=Boolean(False))),
))
    )
    relay = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='relay')
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('owner', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='owner', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    repository_owner = sgqlc.types.Field('RepositoryOwner', graphql_name='repositoryOwner', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    resource = sgqlc.types.Field('UniformResourceLocatable', graphql_name='resource', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(URI), graphql_name='url', default=None)),
))
    )
    search = sgqlc.types.Field(sgqlc.types.non_null('SearchResultItemConnection'), graphql_name='search', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(SearchType), graphql_name='type', default=None)),
))
    )
    topic = sgqlc.types.Field('Topic', graphql_name='topic', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    viewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='viewer')


class Node(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UniformResourceLocatable(sgqlc.types.Interface):
    __schema__ = github_schema
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Actor(sgqlc.types.Interface):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ProjectOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    project = sgqlc.types.Field('Project', graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null('ProjectConnection'), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')


class Closable(sgqlc.types.Interface):
    __schema__ = github_schema
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')


class Updatable(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')


class ProjectColumnConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumnEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumn'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectColumnEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectColumn', graphql_name='node')


class ProjectCardConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectCardEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectCard'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectCardEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectCard', graphql_name='node')


class Assignable(sgqlc.types.Interface):
    __schema__ = github_schema
    assignees = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')


class PageInfo(sgqlc.types.Type):
    __schema__ = github_schema
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class Comment(sgqlc.types.Interface):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    user_content_edits = sgqlc.types.Field('UserContentEditConnection', graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class UserContentEditConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserContentEditEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserContentEdit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserContentEditEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserContentEdit', graphql_name='node')


class UpdatableComment(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')


class Labelable(sgqlc.types.Interface):
    __schema__ = github_schema
    labels = sgqlc.types.Field('LabelConnection', graphql_name='labels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class LabelConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('LabelEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Label'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LabelEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Label', graphql_name='node')


class IssueConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Issue'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Issue', graphql_name='node')


class PullRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequest', graphql_name='node')


class Lockable(sgqlc.types.Interface):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')


class Reactable(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionGroup')), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null('ReactionConnection'), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')


class ReactionGroup(sgqlc.types.Type):
    __schema__ = github_schema
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='subject')
    users = sgqlc.types.Field(sgqlc.types.non_null('ReactingUserConnection'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class ReactingUserConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactingUserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReactingUserEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    reacted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='reactedAt')


class ReactionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Reaction'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class ReactionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Reaction', graphql_name='node')


class RepositoryNode(sgqlc.types.Interface):
    __schema__ = github_schema
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class Subscribable(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')


class GitObject(sgqlc.types.Interface):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class TreeEntry(sgqlc.types.Type):
    __schema__ = github_schema
    mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mode')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    object = sgqlc.types.Field(GitObject, graphql_name='object')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class GitActor(sgqlc.types.Type):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    date = sgqlc.types.Field(GitTimestamp, graphql_name='date')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    user = sgqlc.types.Field('User', graphql_name='user')


class CommitConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Commit', graphql_name='node')


class CommitHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of(CommitEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CommitComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CommitComment', graphql_name='node')


class Deletable(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')


class GitSignature(sgqlc.types.Interface):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')


class Blame(sgqlc.types.Type):
    __schema__ = github_schema
    ranges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BlameRange'))), graphql_name='ranges')


class BlameRange(sgqlc.types.Type):
    __schema__ = github_schema
    age = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='age')
    commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='commit')
    ending_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endingLine')
    starting_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startingLine')


class RepositoryOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    pinned_repositories = sgqlc.types.Field(sgqlc.types.non_null('RepositoryConnection'), graphql_name='pinnedRepositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
))
    )
    repositories = sgqlc.types.Field(sgqlc.types.non_null('RepositoryConnection'), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_disk_usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDiskUsage')


class RepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Repository', graphql_name='node')


class IssueCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueComment', graphql_name='node')


class PullRequestReviewConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReview'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReview', graphql_name='node')


class PullRequestReviewCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReviewComment', graphql_name='node')


class TeamConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Team', graphql_name='node')


class TeamMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamMemberEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    member_access_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessResourcePath')
    member_access_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessUrl')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberRole), graphql_name='role')


class TeamRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamRepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')


class ProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Project'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')


class OrganizationInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationInvitationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class OrganizationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')


class MarketplaceCategory(sgqlc.types.Type):
    __schema__ = github_schema
    description = sgqlc.types.Field(String, graphql_name='description')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    primary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='primaryListingCount')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    secondary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secondaryListingCount')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class LanguageConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('LanguageEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Language'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalSize')


class LanguageEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Language'), graphql_name='node')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')


class ExternalIdentityConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentity'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ExternalIdentityEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ExternalIdentity', graphql_name='node')


class ExternalIdentitySamlAttributes(sgqlc.types.Type):
    __schema__ = github_schema
    name_id = sgqlc.types.Field(String, graphql_name='nameId')


class ExternalIdentityScimAttributes(sgqlc.types.Type):
    __schema__ = github_schema
    username = sgqlc.types.Field(String, graphql_name='username')


class GistConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Gist'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Gist', graphql_name='node')


class Starrable(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null('StargazerConnection'), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class StargazerConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('StargazerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StargazerEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class GistCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('GistComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('GistComment', graphql_name='node')


class PullRequestCommitConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestCommitEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestCommit', graphql_name='node')


class ReviewRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewRequestEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewRequest', graphql_name='node')


class PullRequestTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestTimelineItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestTimelineItem', graphql_name='node')


class DeploymentStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatusEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatus'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentStatusEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeploymentStatus', graphql_name='node')


class SuggestedReviewer(sgqlc.types.Type):
    __schema__ = github_schema
    is_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthor')
    is_commenter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCommenter')
    reviewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reviewer')


class IssueTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueTimelineItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueTimelineItem', graphql_name='node')


class RepositoryInfo(sgqlc.types.Interface):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    license_info = sgqlc.types.Field('License', graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    owner = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOwner), graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=Int(200))),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class License(sgqlc.types.Type):
    __schema__ = github_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LicenseRule')), graphql_name='conditions')
    description = sgqlc.types.Field(String, graphql_name='description')
    featured = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='featured')
    hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hidden')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    implementation = sgqlc.types.Field(String, graphql_name='implementation')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    limitations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LicenseRule')), graphql_name='limitations')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('LicenseRule')), graphql_name='permissions')
    spdx_id = sgqlc.types.Field(String, graphql_name='spdxId')
    url = sgqlc.types.Field(URI, graphql_name='url')


class LicenseRule(sgqlc.types.Type):
    __schema__ = github_schema
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class DeployKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeployKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeployKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeployKeyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeployKey', graphql_name='node')


class RepositoryTopicConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopicEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopic'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryTopicEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryTopic', graphql_name='node')


class ReleaseAssetConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAssetEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAsset'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseAssetEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReleaseAsset', graphql_name='node')


class ProtectedBranchConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProtectedBranchEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProtectedBranch'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProtectedBranchEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProtectedBranch', graphql_name='node')


class ReviewDismissalAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewDismissalAllowanceEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewDismissalAllowance', graphql_name='node')


class PushAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PushAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PushAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PushAllowanceEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PushAllowance', graphql_name='node')


class MilestoneConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('MilestoneEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Milestone'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MilestoneEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Milestone', graphql_name='node')


class CodeOfConduct(sgqlc.types.Type):
    __schema__ = github_schema
    body = sgqlc.types.Field(String, graphql_name='body')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(URI, graphql_name='url')


class RepositoryCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryCollaboratorEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')


class RefConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RefEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Ref'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RefEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Ref', graphql_name='node')


class ReleaseConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Release'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Release', graphql_name='node')


class DeploymentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Deployment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Deployment', graphql_name='node')


class TopicConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TopicEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Topic'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TopicEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Topic', graphql_name='node')


class PublicKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PublicKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PublicKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PublicKeyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PublicKey', graphql_name='node')


class FollowingConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of(UserEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FollowerConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of(UserEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StarredRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('StarredRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StarredRepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class RateLimit(sgqlc.types.Type):
    __schema__ = github_schema
    cost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cost')
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')
    node_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nodeCount')
    remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remaining')
    reset_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='resetAt')


class SearchResultItemConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItemEdge'), graphql_name='edges')
    issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issueCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    repository_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryCount')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')
    wiki_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wikiCount')


class SearchResultItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SearchResultItem', graphql_name='node')
    text_matches = sgqlc.types.Field(sgqlc.types.list_of('TextMatch'), graphql_name='textMatches')


class TextMatch(sgqlc.types.Type):
    __schema__ = github_schema
    fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fragment')
    highlights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('TextMatchHighlight')), graphql_name='highlights')
    property = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='property')


class TextMatchHighlight(sgqlc.types.Type):
    __schema__ = github_schema
    begin_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='beginIndice')
    end_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endIndice')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')


class MarketplaceListingConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListingEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListing'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketplaceListingEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('MarketplaceListing', graphql_name='node')


class GitHubMetadata(sgqlc.types.Type):
    __schema__ = github_schema
    git_hub_services_sha = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gitHubServicesSha')
    git_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gitIpAddresses')
    hook_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hookIpAddresses')
    importer_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='importerIpAddresses')
    is_password_authentication_verifiable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPasswordAuthenticationVerifiable')
    pages_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pagesIpAddresses')


class Mutation(sgqlc.types.Type):
    __schema__ = github_schema
    accept_topic_suggestion = sgqlc.types.Field('AcceptTopicSuggestionPayload', graphql_name='acceptTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    add_comment = sgqlc.types.Field('AddCommentPayload', graphql_name='addComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCommentInput), graphql_name='input', default=None)),
))
    )
    add_project_card = sgqlc.types.Field('AddProjectCardPayload', graphql_name='addProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectCardInput), graphql_name='input', default=None)),
))
    )
    add_project_column = sgqlc.types.Field('AddProjectColumnPayload', graphql_name='addProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectColumnInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review = sgqlc.types.Field('AddPullRequestReviewPayload', graphql_name='addPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review_comment = sgqlc.types.Field('AddPullRequestReviewCommentPayload', graphql_name='addPullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    add_reaction = sgqlc.types.Field('AddReactionPayload', graphql_name='addReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddReactionInput), graphql_name='input', default=None)),
))
    )
    add_star = sgqlc.types.Field('AddStarPayload', graphql_name='addStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddStarInput), graphql_name='input', default=None)),
))
    )
    create_project = sgqlc.types.Field('CreateProjectPayload', graphql_name='createProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectInput), graphql_name='input', default=None)),
))
    )
    decline_topic_suggestion = sgqlc.types.Field('DeclineTopicSuggestionPayload', graphql_name='declineTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeclineTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    delete_project = sgqlc.types.Field('DeleteProjectPayload', graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectInput), graphql_name='input', default=None)),
))
    )
    delete_project_card = sgqlc.types.Field('DeleteProjectCardPayload', graphql_name='deleteProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectCardInput), graphql_name='input', default=None)),
))
    )
    delete_project_column = sgqlc.types.Field('DeleteProjectColumnPayload', graphql_name='deleteProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectColumnInput), graphql_name='input', default=None)),
))
    )
    delete_pull_request_review = sgqlc.types.Field('DeletePullRequestReviewPayload', graphql_name='deletePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    dismiss_pull_request_review = sgqlc.types.Field('DismissPullRequestReviewPayload', graphql_name='dismissPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DismissPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    lock_lockable = sgqlc.types.Field('LockLockablePayload', graphql_name='lockLockable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LockLockableInput), graphql_name='input', default=None)),
))
    )
    move_project_card = sgqlc.types.Field('MoveProjectCardPayload', graphql_name='moveProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveProjectCardInput), graphql_name='input', default=None)),
))
    )
    move_project_column = sgqlc.types.Field('MoveProjectColumnPayload', graphql_name='moveProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveProjectColumnInput), graphql_name='input', default=None)),
))
    )
    remove_outside_collaborator = sgqlc.types.Field('RemoveOutsideCollaboratorPayload', graphql_name='removeOutsideCollaborator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveOutsideCollaboratorInput), graphql_name='input', default=None)),
))
    )
    remove_reaction = sgqlc.types.Field('RemoveReactionPayload', graphql_name='removeReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveReactionInput), graphql_name='input', default=None)),
))
    )
    remove_star = sgqlc.types.Field('RemoveStarPayload', graphql_name='removeStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveStarInput), graphql_name='input', default=None)),
))
    )
    request_reviews = sgqlc.types.Field('RequestReviewsPayload', graphql_name='requestReviews', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RequestReviewsInput), graphql_name='input', default=None)),
))
    )
    submit_pull_request_review = sgqlc.types.Field('SubmitPullRequestReviewPayload', graphql_name='submitPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SubmitPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    update_project = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectInput), graphql_name='input', default=None)),
))
    )
    update_project_card = sgqlc.types.Field('UpdateProjectCardPayload', graphql_name='updateProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectCardInput), graphql_name='input', default=None)),
))
    )
    update_project_column = sgqlc.types.Field('UpdateProjectColumnPayload', graphql_name='updateProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectColumnInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review = sgqlc.types.Field('UpdatePullRequestReviewPayload', graphql_name='updatePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review_comment = sgqlc.types.Field('UpdatePullRequestReviewCommentPayload', graphql_name='updatePullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    update_subscription = sgqlc.types.Field('UpdateSubscriptionPayload', graphql_name='updateSubscription', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSubscriptionInput), graphql_name='input', default=None)),
))
    )
    update_topics = sgqlc.types.Field('UpdateTopicsPayload', graphql_name='updateTopics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTopicsInput), graphql_name='input', default=None)),
))
    )


class AddReactionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field(sgqlc.types.non_null('Reaction'), graphql_name='reaction')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='subject')


class RemoveReactionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field(sgqlc.types.non_null('Reaction'), graphql_name='reaction')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='subject')


class UpdateSubscriptionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class AddCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_edge = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentEdge), graphql_name='commentEdge')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Node), graphql_name='subject')
    timeline_edge = sgqlc.types.Field(sgqlc.types.non_null(IssueTimelineItemEdge), graphql_name='timelineEdge')


class CreateProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class UpdateProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class DeleteProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field(sgqlc.types.non_null(ProjectOwner), graphql_name='owner')


class AddProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field(sgqlc.types.non_null(ProjectColumnEdge), graphql_name='columnEdge')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class MoveProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field(sgqlc.types.non_null(ProjectColumnEdge), graphql_name='columnEdge')


class UpdateProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field(sgqlc.types.non_null('ProjectColumn'), graphql_name='projectColumn')


class DeleteProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='deletedColumnId')
    project = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='project')


class AddProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    card_edge = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardEdge), graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field(sgqlc.types.non_null('Project'), graphql_name='projectColumn')


class UpdateProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card = sgqlc.types.Field(sgqlc.types.non_null('ProjectCard'), graphql_name='projectCard')


class MoveProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    card_edge = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardEdge), graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column = sgqlc.types.Field(sgqlc.types.non_null('ProjectColumn'), graphql_name='column')
    deleted_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='deletedCardId')


class LockLockablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    locked_record = sgqlc.types.Field(Lockable, graphql_name='lockedRecord')


class AddPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')
    review_edge = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewEdge), graphql_name='reviewEdge')


class SubmitPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')


class UpdatePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')


class DismissPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')


class DeletePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')


class AddPullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReviewComment'), graphql_name='comment')
    comment_edge = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentEdge), graphql_name='commentEdge')


class UpdatePullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_comment = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReviewComment'), graphql_name='pullRequestReviewComment')


class RemoveOutsideCollaboratorPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    removed_user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='removedUser')


class RequestReviewsPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    requested_reviewers_edge = sgqlc.types.Field(sgqlc.types.non_null(UserEdge), graphql_name='requestedReviewersEdge')


class AddStarPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field(sgqlc.types.non_null(Starrable), graphql_name='starrable')


class RemoveStarPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field(sgqlc.types.non_null(Starrable), graphql_name='starrable')


class AcceptTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    topic = sgqlc.types.Field(sgqlc.types.non_null('Topic'), graphql_name='topic')


class DeclineTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    topic = sgqlc.types.Field(sgqlc.types.non_null('Topic'), graphql_name='topic')


class UpdateTopicsPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invalid_topic_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='invalidTopicNames')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class User(sgqlc.types.Type, Node, Actor, RepositoryOwner, UniformResourceLocatable):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    bio = sgqlc.types.Field(String, graphql_name='bio')
    bio_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bioHTML')
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    company = sgqlc.types.Field(String, graphql_name='company')
    company_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='companyHTML')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    followers = sgqlc.types.Field(sgqlc.types.non_null(FollowerConnection), graphql_name='followers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    following = sgqlc.types.Field(sgqlc.types.non_null(FollowingConnection), graphql_name='following', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    gist = sgqlc.types.Field('Gist', graphql_name='gist', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    gist_comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='gistComments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    gists = sgqlc.types.Field(sgqlc.types.non_null(GistConnection), graphql_name='gists', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(GistPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(GistOrder, graphql_name='orderBy', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_bounty_hunter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBountyHunter')
    is_campus_expert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCampusExpert')
    is_developer_program_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeveloperProgramMember')
    is_employee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmployee')
    is_hireable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHireable')
    is_site_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSiteAdmin')
    is_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isViewer')
    issue_comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='issueComments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
))
    )
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field('Organization', graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    pinned_repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='pinnedRepositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
))
    )
    public_keys = sgqlc.types.Field(sgqlc.types.non_null(PublicKeyConnection), graphql_name='publicKeys', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repositories_contributed_to = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositoriesContributedTo', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('include_user_repositories', sgqlc.types.Arg(Boolean, graphql_name='includeUserRepositories', default=None)),
        ('contribution_types', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryContributionType), graphql_name='contributionTypes', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    starred_repositories = sgqlc.types.Field(sgqlc.types.non_null(StarredRepositoryConnection), graphql_name='starredRepositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('owned_by_viewer', sgqlc.types.Arg(Boolean, graphql_name='ownedByViewer', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_follow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanFollow')
    viewer_is_following = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsFollowing')
    watching = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='watching', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
))
    )
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class Repository(sgqlc.types.Type, Node, ProjectOwner, Subscribable, Starrable, UniformResourceLocatable, RepositoryInfo):
    __schema__ = github_schema
    assignable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignableUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    code_of_conduct = sgqlc.types.Field(CodeOfConduct, graphql_name='codeOfConduct')
    collaborators = sgqlc.types.Field(RepositoryCollaboratorConnection, graphql_name='collaborators', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('affiliation', sgqlc.types.Arg(CollaboratorAffiliation, graphql_name='affiliation', default=None)),
))
    )
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    default_branch_ref = sgqlc.types.Field('Ref', graphql_name='defaultBranchRef')
    deploy_keys = sgqlc.types.Field(sgqlc.types.non_null(DeployKeyConnection), graphql_name='deployKeys', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    deployments = sgqlc.types.Field(sgqlc.types.non_null(DeploymentConnection), graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('environments', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='environments', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    disk_usage = sgqlc.types.Field(Int, graphql_name='diskUsage')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    forks = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='forks', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
))
    )
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    issue = sgqlc.types.Field('Issue', graphql_name='issue', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issue_or_pull_request = sgqlc.types.Field('IssueOrPullRequest', graphql_name='issueOrPullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
))
    )
    label = sgqlc.types.Field('Label', graphql_name='label', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    languages = sgqlc.types.Field(LanguageConnection, graphql_name='languages', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(LanguageOrder, graphql_name='orderBy', default=None)),
))
    )
    license_info = sgqlc.types.Field(License, graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mentionable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='mentionableUsers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    milestones = sgqlc.types.Field(MilestoneConnection, graphql_name='milestones', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    object = sgqlc.types.Field(GitObject, graphql_name='object', args=sgqlc.types.ArgDict((
        ('oid', sgqlc.types.Arg(GitObjectID, graphql_name='oid', default=None)),
        ('expression', sgqlc.types.Arg(String, graphql_name='expression', default=None)),
))
    )
    owner = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOwner), graphql_name='owner')
    parent = sgqlc.types.Field('Repository', graphql_name='parent')
    primary_language = sgqlc.types.Field('Language', graphql_name='primaryLanguage')
    project = sgqlc.types.Field('Project', graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    protected_branches = sgqlc.types.Field(sgqlc.types.non_null(ProtectedBranchConnection), graphql_name='protectedBranches', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    ref = sgqlc.types.Field('Ref', graphql_name='ref', args=sgqlc.types.ArgDict((
        ('qualified_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qualifiedName', default=None)),
))
    )
    refs = sgqlc.types.Field(RefConnection, graphql_name='refs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('ref_prefix', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refPrefix', default=None)),
        ('direction', sgqlc.types.Arg(OrderDirection, graphql_name='direction', default=None)),
        ('order_by', sgqlc.types.Arg(RefOrder, graphql_name='orderBy', default=None)),
))
    )
    release = sgqlc.types.Field('Release', graphql_name='release', args=sgqlc.types.ArgDict((
        ('tag_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tagName', default=None)),
))
    )
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(ReleaseOrder, graphql_name='orderBy', default=None)),
))
    )
    repository_topics = sgqlc.types.Field(sgqlc.types.non_null(RepositoryTopicConnection), graphql_name='repositoryTopics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=Int(200))),
))
    )
    ssh_url = sgqlc.types.Field(sgqlc.types.non_null(GitSSHRemote), graphql_name='sshUrl')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update_topics = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdateTopics')
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')
    watchers = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='watchers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class Project(sgqlc.types.Type, Node, Closable, Updatable):
    __schema__ = github_schema
    body = sgqlc.types.Field(String, graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    columns = sgqlc.types.Field(sgqlc.types.non_null(ProjectColumnConnection), graphql_name='columns', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    owner = sgqlc.types.Field(sgqlc.types.non_null(ProjectOwner), graphql_name='owner')
    pending_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='pendingCards', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(ProjectState), graphql_name='state')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')


class ProjectColumn(sgqlc.types.Type, Node):
    __schema__ = github_schema
    cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='cards', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ProjectCard(sgqlc.types.Type, Node):
    __schema__ = github_schema
    column = sgqlc.types.Field(ProjectColumn, graphql_name='column')
    content = sgqlc.types.Field('ProjectCardItem', graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    note = sgqlc.types.Field(String, graphql_name='note')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(ProjectCardState, graphql_name='state')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Issue(sgqlc.types.Type, Node, Assignable, Closable, Comment, Updatable, UpdatableComment, Labelable, Lockable, Reactable, RepositoryNode, Subscribable, UniformResourceLocatable):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    project_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='projectCards', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(IssueState), graphql_name='state')
    timeline = sgqlc.types.Field(sgqlc.types.non_null(IssueTimelineConnection), graphql_name='timeline', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')


class UserContentEdit(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Label(sgqlc.types.Type, Node):
    __schema__ = github_schema
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class PullRequest(sgqlc.types.Type, Node, Assignable, Closable, Comment, Updatable, UpdatableComment, Labelable, Lockable, Reactable, RepositoryNode, Subscribable, UniformResourceLocatable):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    base_ref = sgqlc.types.Field('Ref', graphql_name='baseRef')
    base_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='baseRefName')
    base_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='baseRefOid')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    changed_files = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='changedFiles')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    commits = sgqlc.types.Field(sgqlc.types.non_null(PullRequestCommitConnection), graphql_name='commits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    head_ref = sgqlc.types.Field('Ref', graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    head_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='headRefOid')
    head_repository = sgqlc.types.Field(Repository, graphql_name='headRepository')
    head_repository_owner = sgqlc.types.Field(RepositoryOwner, graphql_name='headRepositoryOwner')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')
    merge_commit = sgqlc.types.Field('Commit', graphql_name='mergeCommit')
    mergeable = sgqlc.types.Field(sgqlc.types.non_null(MergeableState), graphql_name='mergeable')
    merged = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merged')
    merged_at = sgqlc.types.Field(DateTime, graphql_name='mergedAt')
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    potential_merge_commit = sgqlc.types.Field('Commit', graphql_name='potentialMergeCommit')
    project_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='projectCards', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    revert_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertResourcePath')
    revert_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertUrl')
    review_requests = sgqlc.types.Field(ReviewRequestConnection, graphql_name='reviewRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='reviews', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestReviewState)), graphql_name='states', default=None)),
        ('author', sgqlc.types.Arg(String, graphql_name='author', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestState), graphql_name='state')
    suggested_reviewers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SuggestedReviewer)), graphql_name='suggestedReviewers')
    timeline = sgqlc.types.Field(sgqlc.types.non_null(PullRequestTimelineConnection), graphql_name='timeline', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')


class Reaction(sgqlc.types.Type, Node):
    __schema__ = github_schema
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reactable = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='reactable')
    user = sgqlc.types.Field(User, graphql_name='user')


class Ref(sgqlc.types.Type, Node):
    __schema__ = github_schema
    associated_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='associatedPullRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prefix')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='target')


class Commit(sgqlc.types.Type, Node, GitObject, Subscribable):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    author = sgqlc.types.Field(GitActor, graphql_name='author')
    authored_by_committer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='authoredByCommitter')
    authored_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='authoredDate')
    blame = sgqlc.types.Field(sgqlc.types.non_null(Blame), graphql_name='blame', args=sgqlc.types.ArgDict((
        ('path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='path', default=None)),
))
    )
    changed_files = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='changedFiles')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    committed_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='committedDate')
    committed_via_web = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='committedViaWeb')
    committer = sgqlc.types.Field(GitActor, graphql_name='committer')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    history = sgqlc.types.Field(sgqlc.types.non_null(CommitHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('author', sgqlc.types.Arg(CommitAuthor, graphql_name='author', default=None)),
        ('since', sgqlc.types.Arg(GitTimestamp, graphql_name='since', default=None)),
        ('until', sgqlc.types.Arg(GitTimestamp, graphql_name='until', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    message_body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageBody')
    message_body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageBodyHTML')
    message_headline = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageHeadline')
    message_headline_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageHeadlineHTML')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    parents = sgqlc.types.Field(sgqlc.types.non_null(CommitConnection), graphql_name='parents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    pushed_date = sgqlc.types.Field(DateTime, graphql_name='pushedDate')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    signature = sgqlc.types.Field(GitSignature, graphql_name='signature')
    status = sgqlc.types.Field('Status', graphql_name='status')
    tarball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='tarballUrl')
    tree = sgqlc.types.Field(sgqlc.types.non_null('Tree'), graphql_name='tree')
    tree_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeResourcePath')
    tree_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')
    zipball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='zipballUrl')


class Tree(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    entries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TreeEntry)), graphql_name='entries')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class CommitComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class Status(sgqlc.types.Type, Node):
    __schema__ = github_schema
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field('StatusContext', graphql_name='context', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    contexts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatusContext'))), graphql_name='contexts')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')


class StatusContext(sgqlc.types.Type, Node):
    __schema__ = github_schema
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')
    target_url = sgqlc.types.Field(URI, graphql_name='targetUrl')


class Blob(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    byte_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='byteSize')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_binary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBinary')
    is_truncated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTruncated')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    text = sgqlc.types.Field(String, graphql_name='text')


class Milestone(sgqlc.types.Type, Node, Closable, UniformResourceLocatable):
    __schema__ = github_schema
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    due_on = sgqlc.types.Field(DateTime, graphql_name='dueOn')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
))
    )
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(MilestoneState), graphql_name='state')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class IssueComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field(PullRequest, graphql_name='pullRequest')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestReview(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='state')
    submitted_at = sgqlc.types.Field(DateTime, graphql_name='submittedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestReviewComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    diff_hunk = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='diffHunk')
    drafted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='draftedAt')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    original_commit = sgqlc.types.Field(Commit, graphql_name='originalCommit')
    original_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='originalPosition')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_review = sgqlc.types.Field(PullRequestReview, graphql_name='pullRequestReview')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    reply_to = sgqlc.types.Field('PullRequestReviewComment', graphql_name='replyTo')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestReviewThread(sgqlc.types.Type, Node):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class Team(sgqlc.types.Type, Node, Subscribable):
    __schema__ = github_schema
    ancestors = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    avatar_url = sgqlc.types.Field(URI, graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=Int(400))),
))
    )
    child_teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='childTeams', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('immediate_only', sgqlc.types.Arg(Boolean, graphql_name='immediateOnly', default=Boolean(True))),
))
    )
    combined_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='combinedSlug')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    edit_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamResourcePath')
    edit_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitations = sgqlc.types.Field(OrganizationInvitationConnection, graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('membership', sgqlc.types.Arg(TeamMembershipType, graphql_name='membership', default=TeamMembershipType('ALL'))),
        ('role', sgqlc.types.Arg(TeamMemberRole, graphql_name='role', default=None)),
))
    )
    members_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersResourcePath')
    members_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    parent_team = sgqlc.types.Field('Team', graphql_name='parentTeam')
    privacy = sgqlc.types.Field(sgqlc.types.non_null(TeamPrivacy), graphql_name='privacy')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(TeamRepositoryOrder, graphql_name='orderBy', default=None)),
))
    )
    repositories_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesResourcePath')
    repositories_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='viewerSubscription')


class OrganizationInvitation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitation_type = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationType), graphql_name='invitationType')
    invitee = sgqlc.types.Field(User, graphql_name='invitee')
    inviter = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='inviter')
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    role = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationRole), graphql_name='role')


class Organization(sgqlc.types.Type, Node, Actor, ProjectOwner, RepositoryOwner, UniformResourceLocatable):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    organization_billing_email = sgqlc.types.Field(String, graphql_name='organizationBillingEmail')
    pinned_repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='pinnedRepositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
))
    )
    project = sgqlc.types.Field(Project, graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repository = sgqlc.types.Field(Repository, graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    saml_identity_provider = sgqlc.types.Field('OrganizationIdentityProvider', graphql_name='samlIdentityProvider')
    team = sgqlc.types.Field(Team, graphql_name='team', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('privacy', sgqlc.types.Arg(TeamPrivacy, graphql_name='privacy', default=None)),
        ('role', sgqlc.types.Arg(TeamRole, graphql_name='role', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('ldap_mapped', sgqlc.types.Arg(Boolean, graphql_name='ldapMapped', default=None)),
        ('root_teams_only', sgqlc.types.Arg(Boolean, graphql_name='rootTeamsOnly', default=Boolean(False))),
))
    )
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')
    viewer_can_create_repositories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateRepositories')
    viewer_can_create_teams = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateTeams')
    viewer_is_amember = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsAMember')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class MarketplaceListing(sgqlc.types.Type, Node):
    __schema__ = github_schema
    company_url = sgqlc.types.Field(URI, graphql_name='companyUrl')
    configuration_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationResourcePath')
    configuration_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationUrl')
    documentation_url = sgqlc.types.Field(URI, graphql_name='documentationUrl')
    extended_description = sgqlc.types.Field(String, graphql_name='extendedDescription')
    extended_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='extendedDescriptionHTML')
    full_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullDescription')
    full_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='fullDescriptionHTML')
    has_approval_been_requested = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasApprovalBeenRequested')
    has_published_free_trial_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPublishedFreeTrialPlans')
    has_terms_of_service = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTermsOfService')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    how_it_works_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='howItWorksHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    installation_url = sgqlc.types.Field(URI, graphql_name='installationUrl')
    installed_for_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='installedForViewer')
    is_approved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isApproved')
    is_delisted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDelisted')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaid')
    is_rejected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRejected')
    logo_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoBackgroundColor')
    logo_url = sgqlc.types.Field(URI, graphql_name='logoUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=Int(400))),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    normalized_short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='normalizedShortDescription')
    pricing_url = sgqlc.types.Field(URI, graphql_name='pricingUrl')
    primary_category = sgqlc.types.Field(sgqlc.types.non_null(MarketplaceCategory), graphql_name='primaryCategory')
    privacy_policy_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='privacyPolicyUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    screenshot_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='screenshotUrls')
    secondary_category = sgqlc.types.Field(MarketplaceCategory, graphql_name='secondaryCategory')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    status_url = sgqlc.types.Field(URI, graphql_name='statusUrl')
    support_email = sgqlc.types.Field(String, graphql_name='supportEmail')
    support_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='supportUrl')
    terms_of_service_url = sgqlc.types.Field(URI, graphql_name='termsOfServiceUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_add_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAddPlans')
    viewer_can_approve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanApprove')
    viewer_can_delist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelist')
    viewer_can_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEdit')
    viewer_can_edit_categories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditCategories')
    viewer_can_edit_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditPlans')
    viewer_can_redraft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRedraft')
    viewer_can_reject = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReject')
    viewer_can_request_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRequestApproval')
    viewer_has_purchased = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchased')
    viewer_has_purchased_for_all_organizations = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchasedForAllOrganizations')
    viewer_is_listing_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsListingAdmin')


class Bot(sgqlc.types.Type, Node, Actor, UniformResourceLocatable):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Language(sgqlc.types.Type, Node):
    __schema__ = github_schema
    color = sgqlc.types.Field(String, graphql_name='color')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class OrganizationIdentityProvider(sgqlc.types.Type, Node):
    __schema__ = github_schema
    digest_method = sgqlc.types.Field(URI, graphql_name='digestMethod')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    idp_certificate = sgqlc.types.Field(X509Certificate, graphql_name='idpCertificate')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    signature_method = sgqlc.types.Field(URI, graphql_name='signatureMethod')
    sso_url = sgqlc.types.Field(URI, graphql_name='ssoUrl')


class ExternalIdentity(sgqlc.types.Type, Node):
    __schema__ = github_schema
    guid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='guid')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization_invitation = sgqlc.types.Field(OrganizationInvitation, graphql_name='organizationInvitation')
    saml_identity = sgqlc.types.Field(ExternalIdentitySamlAttributes, graphql_name='samlIdentity')
    scim_identity = sgqlc.types.Field(ExternalIdentityScimAttributes, graphql_name='scimIdentity')
    user = sgqlc.types.Field(User, graphql_name='user')


class Gist(sgqlc.types.Type, Node, Starrable):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field(RepositoryOwner, graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class GistComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    gist = sgqlc.types.Field(sgqlc.types.non_null(Gist), graphql_name='gist')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestCommit(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ReviewRequest(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class CommitCommentThread(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class ClosedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    closer = sgqlc.types.Field('Closer', graphql_name='closer')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ReopenedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class SubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class UnsubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class MergedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    merge_ref = sgqlc.types.Field(Ref, graphql_name='mergeRef')
    merge_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mergeRefName')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ReferencedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    commit_repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='commitRepository')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    is_direct_reference = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirectReference')
    subject = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='subject')


class CrossReferencedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    referenced_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='referencedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    source = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='target')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    will_close_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='willCloseTarget')


class AssignedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(User, graphql_name='user')


class UnassignedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user = sgqlc.types.Field(User, graphql_name='user')


class LabeledEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class UnlabeledEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class MilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class DemilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class RenamedTitleEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentTitle')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    previous_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previousTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('RenamedTitleSubject'), graphql_name='subject')


class LockedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class UnlockedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class DeployedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deployment = sgqlc.types.Field(sgqlc.types.non_null('Deployment'), graphql_name='deployment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    ref = sgqlc.types.Field(Ref, graphql_name='ref')


class Deployment(sgqlc.types.Type, Node):
    __schema__ = github_schema
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    latest_status = sgqlc.types.Field('DeploymentStatus', graphql_name='latestStatus')
    payload = sgqlc.types.Field(String, graphql_name='payload')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    state = sgqlc.types.Field(DeploymentState, graphql_name='state')
    statuses = sgqlc.types.Field(DeploymentStatusConnection, graphql_name='statuses', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class DeploymentStatus(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(Deployment), graphql_name='deployment')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment_url = sgqlc.types.Field(URI, graphql_name='environmentUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    log_url = sgqlc.types.Field(URI, graphql_name='logUrl')
    state = sgqlc.types.Field(sgqlc.types.non_null(DeploymentStatusState), graphql_name='state')


class HeadRefDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    head_ref = sgqlc.types.Field(Ref, graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class HeadRefRestoredEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')


class HeadRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field(Commit, graphql_name='afterCommit')
    before_commit = sgqlc.types.Field(Commit, graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    ref = sgqlc.types.Field(Ref, graphql_name='ref')


class BaseRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field(Commit, graphql_name='afterCommit')
    before_commit = sgqlc.types.Field(Commit, graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    ref = sgqlc.types.Field(Ref, graphql_name='ref')


class ReviewRequestedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewRequestRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewDismissedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    message_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageHtml')
    previous_review_state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='previousReviewState')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_commit = sgqlc.types.Field(PullRequestCommit, graphql_name='pullRequestCommit')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    review = sgqlc.types.Field(PullRequestReview, graphql_name='review')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class BaseRefChangedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AddedToProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CommentDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ConvertedNoteToIssueEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MentionedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MovedColumnsInProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RemovedFromProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeployKey(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    read_only = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readOnly')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verified')


class RepositoryTopic(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    topic = sgqlc.types.Field(sgqlc.types.non_null('Topic'), graphql_name='topic')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Topic(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    related_topics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Topic'))), graphql_name='relatedTopics')


class Release(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    author = sgqlc.types.Field(User, graphql_name='author')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_prerelease = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrerelease')
    name = sgqlc.types.Field(String, graphql_name='name')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    release_assets = sgqlc.types.Field(sgqlc.types.non_null(ReleaseAssetConnection), graphql_name='releaseAssets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    tag = sgqlc.types.Field(Ref, graphql_name='tag')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ReleaseAsset(sgqlc.types.Type, Node):
    __schema__ = github_schema
    content_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentType')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    download_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadCount')
    download_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='downloadUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    release = sgqlc.types.Field(Release, graphql_name='release')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    uploaded_by = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='uploadedBy')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ProtectedBranch(sgqlc.types.Type, Node):
    __schema__ = github_schema
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    has_dismissable_stale_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasDismissableStaleReviews')
    has_required_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasRequiredReviews')
    has_required_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasRequiredStatusChecks')
    has_restricted_pushes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasRestrictedPushes')
    has_restricted_review_dismissals = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasRestrictedReviewDismissals')
    has_strict_required_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasStrictRequiredStatusChecks')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_admin_enforced = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEnforced')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    push_allowances = sgqlc.types.Field(sgqlc.types.non_null(PushAllowanceConnection), graphql_name='pushAllowances', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredStatusCheckContexts')
    review_dismissal_allowances = sgqlc.types.Field(sgqlc.types.non_null(ReviewDismissalAllowanceConnection), graphql_name='reviewDismissalAllowances', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )


class ReviewDismissalAllowance(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field('ReviewDismissalAllowanceActor', graphql_name='actor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protected_branch = sgqlc.types.Field(sgqlc.types.non_null(ProtectedBranch), graphql_name='protectedBranch')


class PushAllowance(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field('PushAllowanceActor', graphql_name='actor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protected_branch = sgqlc.types.Field(sgqlc.types.non_null(ProtectedBranch), graphql_name='protectedBranch')


class PublicKey(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class GpgSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    key_id = sgqlc.types.Field(String, graphql_name='keyId')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field(User, graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')


class RepositoryInvitation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitee = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='invitee')
    inviter = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='inviter')
    repository = sgqlc.types.Field('RepositoryInvitationRepository', graphql_name='repository')


class RepositoryInvitationRepository(sgqlc.types.Type, RepositoryInfo):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    license_info = sgqlc.types.Field(License, graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    owner = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOwner), graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=Int(200))),
))
    )
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class SmimeSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field(User, graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')


class Tag(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(String, graphql_name='message')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    tagger = sgqlc.types.Field(GitActor, graphql_name='tagger')
    target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='target')


class UnknownSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field(User, graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')



########################################################################
# Unions
########################################################################
class ProjectCardItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class RequestedReviewer(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team)


class PullRequestTimelineItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, CommitCommentThread, PullRequestReview, PullRequestReviewThread, PullRequestReviewComment, IssueComment, ClosedEvent, ReopenedEvent, SubscribedEvent, UnsubscribedEvent, MergedEvent, ReferencedEvent, CrossReferencedEvent, AssignedEvent, UnassignedEvent, LabeledEvent, UnlabeledEvent, MilestonedEvent, DemilestonedEvent, RenamedTitleEvent, LockedEvent, UnlockedEvent, DeployedEvent, HeadRefDeletedEvent, HeadRefRestoredEvent, HeadRefForcePushedEvent, BaseRefForcePushedEvent, ReviewRequestedEvent, ReviewRequestRemovedEvent, ReviewDismissedEvent)


class Closer(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, PullRequest)


class ReferencedSubject(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class MilestoneItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class RenamedTitleSubject(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class IssueOrPullRequest(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class IssueTimelineItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, IssueComment, CrossReferencedEvent, ClosedEvent, ReopenedEvent, SubscribedEvent, UnsubscribedEvent, ReferencedEvent, AssignedEvent, UnassignedEvent, LabeledEvent, UnlabeledEvent, MilestonedEvent, DemilestonedEvent, RenamedTitleEvent, LockedEvent, UnlockedEvent)


class ReviewDismissalAllowanceActor(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team)


class PushAllowanceActor(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team)


class SearchResultItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest, Repository, User, Organization, MarketplaceListing)


