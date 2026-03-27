# Copilot Instructions for sgqlc

## Project Overview

**sgqlc** is a Simple GraphQL Client for Python. It lets you declare GraphQL
schemas as Python classes, generate queries dynamically, and access results
as native Python objects — no raw GraphQL strings needed.

Key modules:

| Module | Purpose |
|--------|---------|
| `sgqlc.types` | Declare types: `Type`, `Interface`, `Enum`, `Union`, `Input`, `Field`, `Arg` |
| `sgqlc.operation` | Build and parse GraphQL operations (queries/mutations/subscriptions) |
| `sgqlc.endpoint` | Access GraphQL APIs: `HTTPEndpoint`, `RequestsEndpoint`, `HTTPXEndpoint`, `WebSocketEndpoint` |
| `sgqlc.introspection` | Introspect schemas via `python -m sgqlc.introspection` |
| `sgqlc.codegen` | Generate Python from GraphQL schemas/operations via `sgqlc-codegen` CLI |
| `sgqlc.types.datetime` | `DateTime`, `Date`, `Time` scalars (ISO 8601) |
| `sgqlc.types.relay` | `Node`, `PageInfo`, `Connection` for Relay pagination |
| `sgqlc.types.uuid` | `UUID` scalar |

## Dev Environment

The project uses **Poetry** for dependency and virtualenv management.

```bash
# Install all dependencies (including dev and all optional extras)
poetry install --all-extras --with dev

# Run any command inside the virtualenv
poetry run <command>

# Install pre-commit hooks (run once after cloning)
pre-commit install
```

## Lint, Format and Test

All quality checks run through **pre-commit**. The CI runs:

```bash
poetry run pre-commit run --hook-stage push --all-files
```

### Formatting

```bash
# Format Python code (Black, 79-char lines, single quotes)
poetry run black sgqlc/ tests/
```

Black settings (in `pyproject.toml`): line-length 79, `skip-string-normalization = true`,
targets Python 3.8–3.13. Schema/operation generated files are excluded.

### Linting

```bash
poetry run flake8 sgqlc/ tests/
```

Flake8 settings (`.flake8`): max-line-length 79, max-complexity 10.
Notable ignored rules: `I801` (isort ordering), `W503` (line break before binary
operator), `N999` (dashes in module names), `A005` (shadowing builtin names like
`http`, `uuid`, `datetime`, `types`).
Print statements are allowed only in `examples/` and `utils/`.

### Testing

```bash
# Run all tests (doctests + unit tests) with coverage
poetry run pytest

# Run a single test file
poetry run pytest tests/test-endpoint-http.py

# Run doctests for a module
poetry run pytest --doctest-modules sgqlc/types/
```

Test configuration (`pyproject.toml`):
- `testpaths = ['sgqlc', 'tests']` — both doctests and unit tests
- `--doctest-modules` is always active
- **100% coverage required** (`--cov-fail-under=100`)
- `asyncio_mode = 'auto'` (pytest-asyncio)
- Test files: `test-*.py` or `test_*.py` (kebab-case preferred)

## Code Guidelines

- Follow **The Zen of Python** (`import this`).
- **Docstrings over comments**: use reStructuredText docstrings that double as
  doctests. Inline comments should be rare and only explain non-obvious logic.
- **Prefer doctests** over unit tests — they document and test simultaneously.
  Use `tests/` files only when mocking or complex setup is needed.
- **Top-level imports** unless there is a specific reason for a local import.
- **Early returns** with the smallest branch (fewest lines of code).
- **No trailing whitespace**, no unused imports, no unused statements.
- Produce code that matches sibling functions in the same file — follow
  existing patterns exactly, do not introduce new ones.
- Use `black` to format. Use `flake8` to verify.
- Documentation: reStructuredText with `:param:`, `:type:`, `:return:`,
  `:rtype:` and cross-references (`:class:`, `:func:`, `:mod:`).
- **Single quotes** for strings (enforced by Black's `skip-string-normalization`).

## Testing Patterns

### Doctests

Most logic is tested via doctests embedded in docstrings. Example from
`sgqlc/types/__init__.py`:

```python
def has_type(self, name):
    '''Check if the type name is known.

    >>> schema = Schema()
    >>> schema.has_type('String')
    True
    '''
```

### Schema Isolation in Tests

Types registered in a `Schema` are global within that schema instance.
If you see `Schema already has XXX` errors, each test must create its own
`Schema()` and declare `__schema__ = newly_created_schema` on types defined
in that test:

```python
def test_something():
    schema = Schema()

    class MyType(sgqlc.types.Type):
        __schema__ = schema
        ...
```

### Unit Tests

Unit tests in `tests/` use pytest and follow the `test-<kebab-name>.py`
naming convention. Use `unittest.mock` or `respx` for HTTP mocking.

## Examples

Examples live in `examples/` and must always run (they are checked in CI).

```bash
# GitHub examples (require GH_TOKEN env var)
export GH_TOKEN=<token>
python3 examples/basic/01_http_endpoint.py $GH_TOKEN profusion/sgqlc

# Shopify examples (require SHOP_STORE and SHOP_TOKEN)
export SHOP_STORE=<store> SHOP_TOKEN=<token>
python3 examples/shopify/...
```

To regenerate generated schema files without live tokens:

```bash
NO_DOWNLOAD=1 ./update-schema.sh
NO_DOWNLOAD=1 ./update-operations.sh
```

**Never disclose** `GH_TOKEN`, `SHOP_STORE`, or `SHOP_TOKEN`.

When the core `sgqlc` library changes, always re-run `./update-schema.sh`
and `./update-operations.sh` to keep generated examples up to date.

## Common Patterns

### Magic methods on types

- `__call__()` — Endpoints are callable
- `__str__()` — Pretty-printed GraphQL output
- `__bytes__()` — Compact GraphQL output
- `__add__()` — Apply operation result (JSON) to produce typed Python objects
- `__iadd__()` — In-place field selection on an operation selector
- `__fields__()` — Bulk field selection by name
- `__alias__()` — Create field aliases
- `__as__()` — Type cast for interfaces

### Code Generation

```bash
# Generate schema Python module from introspection JSON
sgqlc-codegen schema <introspection.json> <output.py>

# Generate operations module from .gql files
sgqlc-codegen operation <schema.py> <output.py> <file.gql> ...
```

## PR and Commit Instructions

- Always run `pre-commit` before committing:
  ```bash
  poetry run pre-commit run -a
  ```
- **Atomic commits**: each commit must pass `pre-commit` on its own.
- Commit message first line: terse, under 72 characters.
- If the commit fixes a GitHub issue, add `Closes: #XXX` as a trailing line.
- If AI-assisted, note it in the commit message.
- Avoid patch-noise: review every changed line — is it really necessary?
- **Do NOT open a Pull Request without prior human review.**
- Do NOT commit secrets, credentials, or generated schema files (they are
  excluded via `.flake8` and `pyproject.toml` `force-exclude`).

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yml`) runs on push to `master`
and on pull requests. It tests Python 3.9–3.13 on ubuntu-latest:

```
poetry install --no-interaction --all-extras --with dev
poetry run pre-commit run --hook-stage push --all-files
```

Coverage is reported to Coveralls (parallel, per-version).

## Directory Structure

```
sgqlc/
├── types/           # Core type system (Schema, Type, Interface, Enum, …)
│   ├── __init__.py  # ~6000 lines — main type system implementation
│   ├── datetime.py  # DateTime/Date/Time scalars
│   ├── relay.py     # Relay pagination types
│   └── uuid.py      # UUID scalar
├── operation/
│   └── __init__.py  # Operation builder and result parser
├── endpoint/
│   ├── base.py      # BaseEndpoint abstract class
│   ├── http.py      # HTTPEndpoint (stdlib urllib)
│   ├── httpx.py     # HTTPXEndpoint (async)
│   ├── requests.py  # RequestsEndpoint
│   └── websocket.py # WebSocketEndpoint (subscriptions)
├── introspection/   # Schema introspection via python -m sgqlc.introspection
└── codegen/         # Code generation: schema.py and operation.py
examples/
├── basic/           # Simple usage examples (no generated schema)
├── github/          # GitHub API (generated github_schema.py)
└── shopify/         # Shopify API (generated shopify_schema.py)
tests/               # Unit tests (test-*.py, kebab-case)
doc/source/          # Sphinx documentation
```

## Known Issues / Workarounds

- **`Schema already has XXX`**: Types are registered globally in a Schema.
  Always create a fresh `Schema()` per test and assign `__schema__` on types.
- **Generated files** (`github_schema.py`, `sample_operations.py`,
  `shopify_schema.py`, `shopify_operations.py`) are excluded from flake8 and
  Black. Do not manually edit them.
- **`NO_DOWNLOAD=1`**: Use this env var with `./update-schema.sh` to
  regenerate schema files without requiring live API tokens.
