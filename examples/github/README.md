Example: Text-based Agile Dashboard for Github Repo
---------------------

Works best if your project is not huge, and makes use of 'milestones'.

Usage:

```bash
poetry install --all-extras
poetry shell
export GH_TOKEN=<your github API token>

cd examples/github
python3 github_agile_dashboard.py --token $GH_TOKEN profusion/sgqlc save data.json
python3 github_agile_dashboard.py --token $GH_TOKEN profusion/sgqlc dashboard --load data.json
```

The output can be filtered by milestone / assignee by doing for example:

```bash
python3 github_agile_dashboard.py --token $GH_TOKEN profusion/sgqlc dashboard --load data.json --assignee barbieri
```

The schema for Github's GraphQL API is encoded locally in `github_schema.json` and `github_schema.py`. To
update those:

```bash
. update-schema.sh
```
