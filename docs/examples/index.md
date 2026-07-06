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
