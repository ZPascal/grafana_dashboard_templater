# Ruff Integration & Documentation Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Modernize the project by replacing flake8 with ruff, raising Python minimum to 3.8, expanding test coverage across recent Python versions, and aligning documentation structure with perses_api_sdk.

**Architecture:** Configuration-first approach: update `pyproject.toml` with Python version and ruff rules, then update CI/CD workflows to use the new config, then build out documentation structure and auto-generation pipeline.

**Tech Stack:** ruff (linting), pydoc-markdown (API doc generation), mkdocs + Material theme (documentation site), pytest (testing)

## Global Constraints

- Python minimum version: 3.8
- Test matrix versions: 3.10, 3.11, 3.12, 3.13, 3.14
- Ruff config must exactly mirror flake8 rules (line-length: 120, same ignore/select)
- Documentation structure must align with perses_api_sdk project
- All auto-commits use GitHub Actions bot account
- 100% code coverage must be maintained

---

## Task 1: Update pyproject.toml — Python Version & Classifiers

**Files:**
- Modify: `pyproject.toml`

**Interfaces:**
- Produces: `requires-python = ">=3.8"` and updated classifiers for Python 3.8–3.14

**Steps:**

- [ ] **Step 1: Open pyproject.toml and locate requires-python line**

Current line (line 13):
```
requires-python = ">=3.6"
```

- [ ] **Step 2: Update requires-python to 3.8**

Replace line 13 with:
```
requires-python = ">=3.8"
```

- [ ] **Step 3: Update classifiers list**

Current classifiers section (lines 14–18):
```python
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved",
    "Operating System :: OS Independent",
]
```

Replace with:
```python
classifiers = [
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "License :: OSI Approved",
    "Operating System :: OS Independent",
]
```

- [ ] **Step 4: Verify changes**

Run: `grep -A 10 "requires-python" pyproject.toml`

Expected output:
```
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3.8",
    ...
    "Programming Language :: Python :: 3.14",
```

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml
git commit -m "chore: bump minimum Python version to 3.8 and update classifiers"
```

---

## Task 2: Add Ruff Configuration to pyproject.toml

**Files:**
- Modify: `pyproject.toml`

**Interfaces:**
- Consumes: Updated pyproject.toml from Task 1
- Produces: `[tool.ruff]` section with exact rules from flake8 config

**Steps:**

- [ ] **Step 1: Locate end of [tool.setuptools] section**

Current file ends with (line 28–29):
```
[tool.setuptools]
packages = ["grafana_dashboard"]
```

- [ ] **Step 2: Add ruff configuration after [tool.setuptools]**

Add to end of file:
```toml

[tool.ruff]
line-length = 120
ignore = ["E203", "E266", "E501", "W503"]
select = ["B", "C", "D", "E", "F", "W", "T4", "B902", "B950"]
exclude = ["venv", ".git"]
```

- [ ] **Step 3: Verify ruff configuration**

Run: `grep -A 6 "\[tool.ruff\]" pyproject.toml`

Expected output:
```
[tool.ruff]
line-length = 120
ignore = ["E203", "E266", "E501", "W503"]
select = ["B", "C", "D", "E", "F", "W", "T4", "B902", "B950"]
exclude = ["venv", ".git"]
```

- [ ] **Step 4: Commit**

```bash
git add pyproject.toml
git commit -m "chore: add ruff linting configuration to pyproject.toml"
```

---

## Task 3: Add Development Dependencies to pyproject.toml

**Files:**
- Modify: `pyproject.toml`

**Interfaces:**
- Consumes: pyproject.toml from Task 2
- Produces: `[project.optional-dependencies]` section with dev tools

**Steps:**

- [ ] **Step 1: Locate [tool.ruff] section added in Task 2**

- [ ] **Step 2: Add optional-dependencies section before [tool.ruff]**

After the `dependencies` list (around line 21), add:
```toml

[project.optional-dependencies]
dev = ["ruff", "pytest", "pytest-cov", "coverage-badge", "pydoc-markdown==4.6.3", "mkdocs", "mkdocs-material"]
```

Full structure should now be:
```
[project]
name = "grafana-dashboard-templater"
...
dependencies = [
    "jinja2",
]

[project.optional-dependencies]
dev = ["ruff", "pytest", "pytest-cov", "coverage-badge", "pydoc-markdown==4.6.3", "mkdocs", "mkdocs-material"]

[project.urls]
...

[tool.setuptools]
...

[tool.ruff]
...
```

- [ ] **Step 3: Verify structure**

Run: `python3 -c "import tomllib; import json; f = open('pyproject.toml', 'rb'); print(json.dumps(tomllib.load(f), indent=2))" | grep -A 10 "optional-dependencies"`

Expected: Shows dev list with all tools

- [ ] **Step 4: Commit**

```bash
git add pyproject.toml
git commit -m "chore: add development dependencies to pyproject.toml"
```

---

## Task 4: Update CI/CD Workflow — Test Job with Python Matrix

**Files:**
- Modify: `.github/workflows/pull-request-checks.yml:9-33` (test job)

**Interfaces:**
- Produces: Test job with matrix for Python 3.10, 3.11, 3.12, 3.13, 3.14

**Steps:**

- [ ] **Step 1: Open .github/workflows/pull-request-checks.yml**

Current test job (lines 9–33):
```yaml
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ '3.10' ]

    steps:
      - uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64
          cache: 'pip'

      - name: Install uv
        uses: astral-sh/setup-uv@v6

      - name: Install the requirements
        run: uv pip install --system .

      - name: Execute the unittests
        run: python3 -m unittest discover tests
```

- [ ] **Step 2: Replace python-version matrix**

Replace line 13 (`python-version: [ '3.10' ]`) with:
```yaml
        python-version: [ '3.10', '3.11', '3.12', '3.13', '3.14' ]
```

- [ ] **Step 3: Verify change**

Run: `grep -A 2 "strategy:" .github/workflows/pull-request-checks.yml | head -5`

Expected:
```
strategy:
  matrix:
    python-version: [ '3.10', '3.11', '3.12', '3.13', '3.14' ]
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/pull-request-checks.yml
git commit -m "ci: expand test matrix to Python 3.10-3.14"
```

---

## Task 5: Update CI/CD Workflow — Replace Flake8 with Ruff

**Files:**
- Modify: `.github/workflows/pull-request-checks.yml:34-63` (lint job)

**Interfaces:**
- Consumes: Ruff config from Task 2 (pyproject.toml)
- Produces: Lint job using ruff instead of flake8

**Steps:**

- [ ] **Step 1: Locate lint job in workflow**

Current lint job (lines 34–63):
```yaml
  lint:
    runs-on: ubuntu-latest
    permissions: write-all
    strategy:
      matrix:
        python-version: [ '3.10' ]

    steps:
      - uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64
          cache: 'pip'

      - name: Install uv
        uses: astral-sh/setup-uv@v6

      - name: Install the requirements
        run: uv pip install --system .

      - name: Execute the linting checks
        uses: reviewdog/action-flake8@v3.15.2
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          flake8_args: --config=.flake8
```

- [ ] **Step 2: Replace linting step with ruff**

Replace the final two steps (`Install the requirements` and `Execute the linting checks`) with:

```yaml
      - name: Install the requirements
        run: uv pip install --system ruff

      - name: Execute the linting checks
        run: ruff check .
```

Full lint job should now be:
```yaml
  lint:
    runs-on: ubuntu-latest
    permissions: write-all
    strategy:
      matrix:
        python-version: [ '3.10' ]

    steps:
      - uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64
          cache: 'pip'

      - name: Install uv
        uses: astral-sh/setup-uv@v6

      - name: Install the requirements
        run: uv pip install --system ruff

      - name: Execute the linting checks
        run: ruff check .
```

- [ ] **Step 3: Verify changes**

Run: `grep -A 3 "Execute the linting checks" .github/workflows/pull-request-checks.yml`

Expected:
```
      - name: Execute the linting checks
        run: ruff check .
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/pull-request-checks.yml
git commit -m "ci: replace flake8 with ruff for linting"
```

---

## Task 6: Update CI/CD Workflow — Coverage Job to Install Ruff

**Files:**
- Modify: `.github/workflows/pull-request-checks.yml:87` (coverage job install step)

**Interfaces:**
- Consumes: Ruff config from Task 2
- Produces: Coverage job installs ruff alongside other dev tools

**Steps:**

- [ ] **Step 1: Locate coverage job install step**

Current line 87:
```yaml
        run: uv pip install --system . pytest pytest-cov coverage-badge
```

- [ ] **Step 2: Add ruff to install list**

Replace line 87 with:
```yaml
        run: uv pip install --system . pytest pytest-cov coverage-badge ruff
```

- [ ] **Step 3: Verify change**

Run: `sed -n '87p' .github/workflows/pull-request-checks.yml`

Expected:
```
        run: uv pip install --system . pytest pytest-cov coverage-badge ruff
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/pull-request-checks.yml
git commit -m "ci: add ruff to coverage job dependencies"
```

---

## Task 7: Update CI/CD Workflow — Documentation Job Structure

**Files:**
- Modify: `.github/workflows/pull-request-checks.yml:127-176` (documentation job)

**Interfaces:**
- Produces: Documentation job with updated pydoc-markdown and mkdocs build

**Steps:**

- [ ] **Step 1: Locate documentation job (starts at line 127)**

Current documentation job runs:
```yaml
      - name: Generate documentation
        run: pydoc-markdown --render-toc && rm -rf docs/content && mv build/docs/* docs
```

- [ ] **Step 2: Update install step to include mkdocs**

Current line 150:
```yaml
        run: uv pip install --system pydoc-markdown==4.6.3 mkdocs mkdocs-material
```

This is already correct (mkdocs and mkdocs-material are included). No change needed to this line.

- [ ] **Step 3: Update generate documentation step**

Replace the `Generate documentation` step (lines 152–153):
```yaml
      - name: Generate documentation
        run: pydoc-markdown --render-toc && rm -rf docs/content && mv build/docs/* docs
```

With:
```yaml
      - name: Generate API documentation
        run: pydoc-markdown --render-toc

      - name: Move API documentation to docs/api
        run: mkdir -p docs/api && mv build/docs/* docs/api/ 2>/dev/null || true

      - name: Build documentation site
        run: mkdocs build
```

Full documentation job should now be:
```yaml
  documentation:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [ '3.9' ]

    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}
          architecture: x64
          cache: 'pip'

      - name: Install uv
        uses: astral-sh/setup-uv@v6

      - name: Install the requirements
        run: uv pip install --system pydoc-markdown==4.6.3 mkdocs mkdocs-material

      - name: Generate API documentation
        run: pydoc-markdown --render-toc

      - name: Move API documentation to docs/api
        run: mkdir -p docs/api && mv build/docs/* docs/api/ 2>/dev/null || true

      - name: Build documentation site
        run: mkdocs build

      - name: Check changed files
        uses: tj-actions/verify-changed-files@v20
        id: verify-changed-files
        with:
          files: |
            docs

      - name: Commit files
        if: steps.verify-changed-files.outputs.files_changed == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add --force docs
          git commit -m "docs: Add the documentation"

      - name: Push changes
        uses: ad-m/github-push-action@master
        if: steps.verify-changed-files.outputs.files_changed == 'true'
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.head_ref }}
```

- [ ] **Step 4: Verify changes**

Run: `grep -A 2 "Generate API documentation" .github/workflows/pull-request-checks.yml`

Expected:
```
      - name: Generate API documentation
        run: pydoc-markdown --render-toc
```

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/pull-request-checks.yml
git commit -m "ci: update documentation job to include mkdocs build and api directory structure"
```

---

## Task 8: Create mkdocs.yml Configuration

**Files:**
- Create: `mkdocs.yml`

**Interfaces:**
- Produces: mkdocs configuration with Material theme

**Steps:**

- [ ] **Step 1: Create mkdocs.yml in repo root**

Create new file `mkdocs.yml` with content:
```yaml
site_name: Grafana Dashboard Templater
site_description: A Grafana dashboard templater
site_url: https://github.com/ZPascal/grafana_dashboard_templater
repo_url: https://github.com/ZPascal/grafana_dashboard_templater
repo_name: grafana_dashboard_templater

theme:
  name: material
  palette:
    scheme: default
  icon:
    repo: fontawesome/brands/github

nav:
  - Home: index.md
  - Installation: installation.md
  - API Reference: api/index.md
  - Examples: examples/index.md
  - Contributing: contributing.md

plugins:
  - search
```

- [ ] **Step 2: Verify file exists**

Run: `test -f mkdocs.yml && echo "File created successfully"`

Expected: "File created successfully"

- [ ] **Step 3: Validate YAML syntax**

Run: `python3 -c "import yaml; yaml.safe_load(open('mkdocs.yml'))" && echo "Valid YAML"`

Expected: "Valid YAML"

- [ ] **Step 4: Commit**

```bash
git add mkdocs.yml
git commit -m "docs: add mkdocs configuration for Material theme"
```

---

## Task 9: Create Documentation — index.md

**Files:**
- Create: `docs/index.md`

**Interfaces:**
- Produces: Project homepage with overview and quick start

**Steps:**

- [ ] **Step 1: Create docs/index.md**

Create new file `docs/index.md` with content:
```markdown
# Grafana Dashboard Templater

A Python utility for templating Grafana dashboards using Jinja2. Generate dynamic dashboards programmatically with data-driven configurations.

## Features

- **Template-based dashboard generation** — Use Jinja2 templates to create reusable dashboard definitions
- **Python 3.8+** — Modern Python support
- **Simple API** — Easy-to-use interface for template rendering
- **Production-ready** — Full test coverage and comprehensive documentation

## Quick Start

### Installation

```bash
pip install grafana-dashboard-templater
```

### Basic Usage

```python
from grafana_dashboard.dashboard import Dashboard

# Create a dashboard from a template
dashboard = Dashboard(
    title="My Dashboard",
    description="A templated dashboard",
    tags=["example"]
)

# Render as JSON
dashboard_json = dashboard.render()
```

For more examples, see the [Examples](examples/index.md) section.

## Getting Help

- **Questions?** See the [Installation Guide](installation.md)
- **API Reference?** Check the [API Documentation](api/index.md)
- **Want to contribute?** Read [Contributing](contributing.md)
- **Found a bug?** [Open an issue](https://github.com/ZPascal/grafana_dashboard_templater/issues)

## License

Licensed under the OSI-approved license. See LICENSE file for details.
```

- [ ] **Step 2: Verify file exists**

Run: `test -f docs/index.md && echo "File created successfully"`

Expected: "File created successfully"

- [ ] **Step 3: Commit**

```bash
git add docs/index.md
git commit -m "docs: create project homepage"
```

---

## Task 10: Create Documentation — installation.md

**Files:**
- Create: `docs/installation.md`

**Interfaces:**
- Produces: Installation and setup guide

**Steps:**

- [ ] **Step 1: Create docs/installation.md**

Create new file `docs/installation.md` with content:
```markdown
# Installation

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installing from PyPI

The easiest way to install grafana-dashboard-templater is from PyPI:

```bash
pip install grafana-dashboard-templater
```

## Installing from Source

To install directly from the GitHub repository:

```bash
git clone https://github.com/ZPascal/grafana_dashboard_templater.git
cd grafana_dashboard_templater
pip install .
```

## Installing with Development Tools

If you want to contribute or run tests locally:

```bash
pip install ".[dev]"
```

This installs the package along with development dependencies:
- `ruff` — Fast Python linter
- `pytest` — Testing framework
- `pytest-cov` — Code coverage for pytest
- `coverage-badge` — Coverage badge generation
- `pydoc-markdown` — API documentation generation
- `mkdocs` — Documentation site builder
- `mkdocs-material` — Material design theme for MkDocs

## Verifying Installation

To verify the installation was successful:

```python
from grafana_dashboard.dashboard import Dashboard
print("Installation successful!")
```

## Next Steps

- Read the [Quick Start](index.md) guide
- Check out [Examples](examples/index.md)
- Review the [API Documentation](api/index.md)
```

- [ ] **Step 2: Verify file exists**

Run: `test -f docs/installation.md && echo "File created successfully"`

Expected: "File created successfully"

- [ ] **Step 3: Commit**

```bash
git add docs/installation.md
git commit -m "docs: create installation guide"
```

---

## Task 11: Create Documentation — contributing.md

**Files:**
- Create: `docs/contributing.md`

**Interfaces:**
- Produces: Contribution guidelines

**Steps:**

- [ ] **Step 1: Create docs/contributing.md**

Create new file `docs/contributing.md` with content:
```markdown
# Contributing

We welcome contributions! Here's how to get started.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/ZPascal/grafana_dashboard_templater.git
cd grafana_dashboard_templater
```

2. Install in development mode:
```bash
pip install ".[dev]"
```

## Running Tests

Run the test suite:

```bash
python3 -m unittest discover tests
```

### Test Coverage

We maintain 100% test coverage. When adding features or fixing bugs, include tests:

```bash
pytest tests/ --cov=grafana_dashboard --cov-report=html
```

## Code Quality

### Linting

We use ruff for code quality checks. Before committing:

```bash
ruff check .
```

Fix any issues reported by ruff.

### Style Guide

- Follow PEP 8
- Use meaningful variable and function names
- Add docstrings to public functions and classes
- Keep functions small and focused

## Documentation

- Update docstrings when changing public APIs
- Add examples to demonstrate new features
- Keep the [Examples](examples/index.md) section current

## Submitting Changes

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes and commit with clear messages
3. Push to your fork: `git push origin feature/my-feature`
4. Open a Pull Request with a clear description

## PR Requirements

- All tests must pass
- Code coverage must remain at 100%
- Ruff linting checks must pass
- Documentation must be updated
- Commits should be clear and atomic

## Questions?

If you have questions, feel free to open an issue or reach out to the maintainers.

Thank you for contributing!
```

- [ ] **Step 2: Verify file exists**

Run: `test -f docs/contributing.md && echo "File created successfully"`

Expected: "File created successfully"

- [ ] **Step 3: Commit**

```bash
git add docs/contributing.md
git commit -m "docs: create contribution guidelines"
```

---

## Task 12: Create Examples Directory and Index

**Files:**
- Create: `docs/examples/index.md`

**Interfaces:**
- Produces: Examples landing page with usage patterns

**Steps:**

- [ ] **Step 1: Create docs/examples directory**

Run: `mkdir -p docs/examples`

- [ ] **Step 2: Create docs/examples/index.md**

Create new file `docs/examples/index.md` with content:
```markdown
# Examples

Learn how to use grafana-dashboard-templater with these examples.

## Basic Dashboard Creation

Here's a simple example of creating a Grafana dashboard:

```python
from grafana_dashboard.dashboard import Dashboard

# Create a new dashboard
dashboard = Dashboard(
    title="My Dashboard",
    description="A simple dashboard example",
    tags=["example", "demo"]
)

# Export as JSON (ready to import into Grafana)
dashboard_json = dashboard.render()
print(dashboard_json)
```

## Using Jinja2 Templates

Leverage Jinja2 templating for dynamic dashboards:

```python
from jinja2 import Template
from grafana_dashboard.dashboard import Dashboard

# Define a template
template_str = """
{
    "title": "{{ dashboard_title }}",
    "description": "{{ dashboard_description }}",
    "tags": {{ tags | tojson }},
    "panels": []
}
"""

template = Template(template_str)
rendered = template.render(
    dashboard_title="Sales Dashboard",
    dashboard_description="Q4 Sales Metrics",
    tags=["sales", "q4"]
)

print(rendered)
```

## More Examples

More comprehensive examples and use cases coming soon. Check the [API Reference](../api/index.md) for detailed documentation.

## Questions?

See the [Installation Guide](../installation.md) or open an issue on GitHub.
```

- [ ] **Step 3: Verify files exist**

Run: `test -d docs/examples && test -f docs/examples/index.md && echo "Examples directory and index created"`

Expected: "Examples directory and index created"

- [ ] **Step 4: Commit**

```bash
git add docs/examples/index.md
git commit -m "docs: create examples directory and index"
```

---

## Task 13: Verify Ruff Works with New Configuration

**Files:**
- No modifications; verification only

**Interfaces:**
- Consumes: pyproject.toml with ruff config from Task 2
- Produces: Verification that ruff runs without errors

**Steps:**

- [ ] **Step 1: Install ruff locally**

Run: `uv pip install ruff`

Expected: Ruff installs successfully

- [ ] **Step 2: Run ruff check on the codebase**

Run: `ruff check .`

Expected: Either "All checks passed" or reports issues (if any)

- [ ] **Step 3: Verify ruff config is being used**

Run: `ruff check . --show-settings | head -20`

Expected: Output shows configuration from pyproject.toml (line-length: 120, etc.)

- [ ] **Step 4: Run tests to ensure nothing broke**

Run: `python3 -m unittest discover tests`

Expected: All tests pass with same coverage as before

- [ ] **Step 5: No commit needed for verification step**

This is a verification task; no code changes.

---

## Task 14: Verify Documentation Generation

**Files:**
- No modifications; verification only

**Interfaces:**
- Consumes: mkdocs.yml from Task 8, manual docs from Tasks 9–12
- Produces: Verification that mkdocs builds successfully

**Steps:**

- [ ] **Step 1: Install mkdocs dependencies**

Run: `uv pip install mkdocs mkdocs-material pydoc-markdown==4.6.3`

Expected: All packages install successfully

- [ ] **Step 2: Generate pydoc-markdown docs**

Run: `pydoc-markdown --render-toc`

Expected: Generates API documentation in build/docs/

- [ ] **Step 3: Move API docs to docs/api**

Run: `mkdir -p docs/api && mv build/docs/* docs/api/ 2>/dev/null || true`

Expected: API docs are now in docs/api/

- [ ] **Step 4: Build mkdocs site**

Run: `mkdocs build`

Expected: Builds successfully, generates site/ directory

- [ ] **Step 5: Verify site was generated**

Run: `test -d site && test -f site/index.html && echo "Documentation site built successfully"`

Expected: "Documentation site built successfully"

- [ ] **Step 6: No commit needed for verification step**

This is a verification task; no code changes.

---

## Self-Review Checklist

**Spec Coverage:**
- ✓ Python version bump to 3.8 (Task 1)
- ✓ Ruff configuration (Tasks 2, 5)
- ✓ CI/CD test matrix (Task 4)
- ✓ Replace flake8 with ruff (Task 5)
- ✓ Documentation structure alignment (Tasks 8–12)
- ✓ mkdocs configuration (Task 8)
- ✓ Dev dependencies (Task 3)
- ✓ Verification of changes (Tasks 13–14)

**Placeholder Scan:**
- ✓ No TBD, TODO, or incomplete sections
- ✓ All steps contain complete code
- ✓ All commands show expected output
- ✓ All file paths are exact

**Type Consistency:**
- ✓ All file paths match across tasks
- ✓ Ruff configuration rules consistent between Task 2 and Task 5
- ✓ Documentation structure matches mkdocs config
- ✓ Dev dependencies in Task 3 match workflow installs in Tasks 6–7

**Execution Order:**
- ✓ pyproject.toml changes (Tasks 1–3) before workflow changes (Tasks 4–7)
- ✓ mkdocs config (Task 8) before documentation content (Tasks 9–12)
- ✓ Verification tasks (Tasks 13–14) at end after all changes

---

## Summary

**14 tasks** organized into logical phases:

1. **Configuration** (Tasks 1–3): Python version, ruff rules, dev dependencies
2. **CI/CD Updates** (Tasks 4–7): Test matrix, linting, coverage, documentation pipeline
3. **Documentation** (Tasks 8–12): mkdocs config and manual documentation files
4. **Verification** (Tasks 13–14): Local testing of ruff and mkdocs builds

All tasks are independent once dependencies are satisfied, enabling parallel execution where appropriate.
