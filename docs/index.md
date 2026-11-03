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
