# Instructions to AI Agents

## Dev environment

* The project manages dependencies, virtual environment and installation using `poetry`. Always use `poetry run` to call commands in the virtual environment.
* This Python 3 project uses PEP8 and best practices.
* The project uses [pre-commit](https://pre-commit.com) to verify `flake8`, `black`, check examples and run tests.
* Format code using `black` and rules defined in `pyproject.toml`, it's executed from `pre-commit` environment/sandbox.
* Quality check and lint is done using `flake8` and rules defined in `.flake8`, it's executed from `pre-commit` environment/sandbox.

## Code Guidelines
* Follow `The Zen of Python, by Tim Peters` (`import this`).
* Do not use useless comments. The code must be legible, thus comments should be mostly useless.
* Use docstrings as a way to document in a testable way. We do not want broken docs.
* Do not leave trailing whitespaces.
* Review every added statement: Is it needed? Is it useful? Is it correct?
* Do not leave useless statements (including imports).
* Use `black` to format.
* Use `flake8` to verify quality and rules.
* Always produce code similar to the sibling statements and functions. Review if same patterns are being followed. Avoid bringing in new patterns.
* Unless explicitly asked, prefer top level imports.
* Unless explicitly asked, prefer early return with the smallest branch (number of lines of code)
* Use reStructuredText documentation.
* See project instructions at `./README.rst`

## Testing instructions
* The project uses `pytest` to run unit tests and doctests.
* Unit tests are stored in `tests/` directory and all have the `test-` prefix followed by a kebab-case descriptive name.
* Doctests are preferred over unit-tests, use it whenever possible. Just use test files when mock and other setup is needed.
* If you receive errors about types being already registered in the schema `Schema already has XXX`, create new `Schema()` in each test and declare `__schema__ = newly_created_schema` for types in that test.
* Test coverage must be 100%, respecting configuration stored at `.coveragerc`.

## Examples instructions
* Meaningful examples stored in `examples/` directory.
* Examples must always be checked as an additional test, they must always run.
* Some examples requires environment variables such as `GH_TOKEN`, `SHOP_STORE` and `SHOP_TOKEN` or arguments such as `--token` to provide per-user, sensitive/private information to run. Never disclose these.
* It's possible to re-run `./update-schema.sh` using `NO_DOWNLOAD=1` environment variables to avoid the requirement of such private tokens. However these will not refresh to the latest API.
* When `sgqlc` is changed, always re-run `./update-schema.sh` and `./update-operations.sh`.

## PR Instructions

* Always run `pre-commit` before creating a commit or push.
* Avoid patch-noise (useless changes), review line by line: "this really needs to be changed?"

* Commits should be atomic: each commit must pass `pre-commit` on its own.
* Commit messages should be brief and meaningful, describing exactly what was done.
* The first line of the commit should be terse and under 72 chars.
* If the commit fixes a bug, add the trailing line: `Closes: #XXX`, where `XXX` is the GitHub issue number.
* Do **NOT** open Pull Request without prior **HUMAN REVIEW**, they will be immediately closed.
* If the commit had AI assistance, write it in the commit message.
