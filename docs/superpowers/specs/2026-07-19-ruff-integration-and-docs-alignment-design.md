# Ruff Integration & Documentation Alignment Design

**Date:** 2026-07-19  
**Status:** Approved  
**Scope:** Modernize linting, align documentation structure with perses_api_sdk, update Python version requirements

---

## Overview

This design modernizes the grafana_dashboard_templater project by:
1. Replacing flake8 with ruff as the single linting tool
2. Raising minimum Python version from 3.6 to 3.8
3. Expanding CI/CD test coverage to Python 3.10–3.14
4. Aligning documentation structure and generation workflow with perses_api_sdk
5. Addressing findings from PR #59

---

## Section 1: Configuration & Python Version Updates

### Changes to `pyproject.toml`

**Python Version Support:**
- Update `requires-python` from `">=3.6"` to `">=3.8"`
- Add explicit classifiers for supported versions:
  ```
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: 3.14",
  ```

**Ruff Configuration:**
- Add `[tool.ruff]` section with rules ported from `.flake8`:
  - `line-length = 120`
  - `ignore = ["E203", "E266", "E501", "W503"]`
  - `select = ["B", "C", "D", "E", "F", "W", "T4", "B902", "B950"]`
  - `exclude = ["venv", ".git"]`

**Development Dependencies:**
- Add `[project.optional-dependencies]` section:
  ```toml
  [project.optional-dependencies]
  dev = ["ruff", "pytest", "pytest-cov", "coverage-badge", "pydoc-markdown", "mkdocs", "mkdocs-material"]
  ```
  - Clarifies tooling needed for local development
  - Allows `pip install .[dev]` for developers

**Deprecation:**
- `.flake8` file remains for reference but is not used in CI/CD or local workflows

---

## Section 2: CI/CD Pipeline Updates

### Test Job
- Add matrix strategy: Python versions `3.10, 3.11, 3.12, 3.13, 3.14`
- All versions run identical test suite: `python3 -m unittest discover tests`
- Enables early detection of version-specific compatibility issues
- Maintains pip cache for performance

### Lint Job
- Replace `reviewdog/action-flake8@v3.15.2` with direct ruff invocation
- Install ruff via uv: `uv pip install --system ruff`
- Run linting: `ruff check .`
- Executes on Python 3.10 (linting is version-agnostic)
- Linting only; no formatting step (keeping code style decisions manual)

### Coverage Job
- Maintain existing pytest-cov workflow
- Generate coverage badge: `coverage-badge -f -o docs/coverage.svg`
- Auto-commit coverage updates to PR if files changed
- Install ruff alongside other dev tools for consistency

### Documentation Job
- Install `pydoc-markdown`, `mkdocs`, `mkdocs-material` via uv
- Generate API docs: `pydoc-markdown --render-toc` → `docs/api/`
- Build site: `mkdocs build` (optional for GitHub Pages)
- Auto-commit documentation changes to PR if files changed

---

## Section 3: Documentation Structure

### Target Structure (aligned with perses_api_sdk)

```
docs/
├── index.md                 # Project overview, quick start
├── installation.md          # Installation & setup
├── contributing.md          # Contribution guidelines
├── api/                     # Auto-generated API documentation
│   └── (pydoc-markdown output)
├── examples/                # Usage examples & tutorials
├── coverage.svg             # Coverage badge (auto-generated)
├── mkdocs.yml              # Navigation & theme config
└── (other generated files)
```

### Configuration Files

**`mkdocs.yml`:**
```yaml
site_name: Grafana Dashboard Templater
site_description: A Grafana dashboard templater
theme:
  name: material
  palette:
    scheme: default
nav:
  - Home: index.md
  - Installation: installation.md
  - API Reference: api/
  - Examples: examples/
  - Contributing: contributing.md
```

### Manual Documentation Files

- **`docs/index.md`:** Project description, features, quick start example
- **`docs/installation.md`:** Installation instructions, basic usage
- **`docs/examples/`:** Tutorial and example use cases
- **`docs/contributing.md`:** Contributing guidelines

### Auto-Generated Files

- **`docs/api/`:** API documentation from docstrings (via pydoc-markdown)
- **`docs/coverage.svg`:** Coverage badge (auto-updated per PR)

---

## Section 4: Testing & Quality Strategy

### Test Coverage
- Maintain 100% code coverage requirement (current baseline)
- Parallel testing across Python 3.10–3.14 via matrix strategy
- Coverage job fails if coverage drops below 100%
- Coverage badge auto-commits to PR branch for visibility

### Linting
- Single source of truth: ruff config in `pyproject.toml`
- Ruff runs on every PR; CI fails if violations found
- Linting-only mode (no formatting enforcement)
- Existing `.flake8` file archived for reference; not used in workflows

### Documentation Quality
- Auto-generated API docs from source docstrings (pydoc-markdown)
- Docs auto-commit ensures code and docs stay synchronized
- Manual docs (index, installation, examples, contributing) maintained separately
- MkDocs Material theme provides consistent, professional appearance

### PR Workflow
All jobs must pass before merge:
1. **test** — all Python versions pass unittest suite
2. **lint** — ruff reports no violations
3. **coverage** — 100% code coverage maintained
4. **documentation** — docs generated and committed if changed

---

## Rationale

**Why Ruff?**
- Faster than flake8 (Rust-based)
- Single tool consolidates all lint rules
- Config lives in `pyproject.toml` (already source of truth)
- Better error messages and documentation

**Why raise Python to 3.8?**
- Python 3.6–3.7 are end-of-life (EOL)
- Aligns with industry standards (3.8+ is baseline for most projects)
- Fixes vague classifiers from PR #59 findings

**Why test 3.10–3.14?**
- Catches version-specific bugs early
- Recent versions; covers modern Python landscape
- Parallel matrix keeps CI time reasonable

**Why align documentation with perses_api_sdk?**
- Consistency across your projects
- Professional, maintainable docs structure
- Leverages proven patterns (mkdocs + Material theme)
- Easier for contributors familiar with your other projects

---

## Implementation Scope

**Files to create/modify:**
- `pyproject.toml` — ruff config, dev dependencies, Python version, classifiers
- `.github/workflows/pull-request-checks.yml` — test matrix, lint→ruff, docs structure
- `.github/workflows/publish-to-pypi.yml` — update if ruff or Python version affects release
- `mkdocs.yml` — new config file
- `docs/index.md`, `docs/installation.md`, `docs/contributing.md` — manual docs
- `docs/examples/` — new directory for examples
- `.flake8` — deprecate (archive content, keep file for reference)

**CI/CD Impact:**
- Slightly longer test time (5 Python versions vs. 1)
- Faster linting (ruff vs. flake8)
- Documentation auto-commits on every PR (similar to current behavior)
- Overall CI time: neutral to slightly faster

**Breaking Changes:**
- None for users (Python 3.8+ is forward-compatible with 3.6 code)
- Local development: developers must use Python 3.8+

---

## Success Criteria

✓ PR #59 findings addressed (Python version classifiers updated)  
✓ Flake8 replaced with ruff; CI passes with zero ruff violations  
✓ Test suite passes on Python 3.10, 3.11, 3.12, 3.13, 3.14  
✓ 100% code coverage maintained  
✓ Documentation structure aligns with perses_api_sdk  
✓ Documentation auto-generated and auto-committed on PRs  
✓ `pyproject.toml` is single source of truth for all config  

---

## Notes

- The `.flake8` file is retained as a historical reference but not used operationally
- Ruff config in `pyproject.toml` exactly mirrors the current `.flake8` rules to avoid behavior changes
- Documentation generation uses the same pydoc-markdown + mkdocs approach as perses_api_sdk
- All auto-commits use the GitHub Actions bot account (existing pattern)
