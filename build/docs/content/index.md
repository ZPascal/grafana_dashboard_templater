# Grafana Dashboard Templater
The Grafana dashboard templater create a valid Grafana dashboard as dictionary based on a template and injected values.

## Dashboard template folder structure

```
dashboard-templates <- Folder of the dashboard templates
     database <- Dashboard type
        postgresql <- Dashboard name
            v13 <- Dashboard version
                dashboard.json.sample <- Dashboard template
```

## Installation

`pip install grafana-dashboard-templater`

## Example

```python
from grafana_dashboard.model import Model
from grafana_dashboard.dashboard import Dashboard

dashboard_model: Model = Model(dashboard_templates_path="./dashboard-templates", dashboard_type="database",
                               dashboard_name="postgresql", dashboard_version="v13")

dashboard: Dashboard = Dashboard(dashboard_model)
dashboard_json = dashboard.get_dashboard_json(template_values={"app_name": "PostgreSQL", "prometheus_name": "k8s-sonarqube-postgresql"})
```

## Grafana API SDK
If you want to establish a connection to Grafana API via an SDK you can check out one of my other [project](https://github.com/ZPascal/grafana_api_sdk) and integrate the functionality inside your code.