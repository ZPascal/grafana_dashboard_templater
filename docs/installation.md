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
