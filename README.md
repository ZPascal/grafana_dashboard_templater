# Grafana dashboard templater ![Coverage report](https://github.com/ZPascal/grafana_dashboard_templater/blob/main/docs/coverage.svg)

## Description

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

## Contribution
If you would like to contribute something, have an improvement request, or want to make a change inside the code, please open a pull request.

## Support
If you need support, or you encounter a bug, please don't hesitate to open an issue.

## Donations
If you would like to support my work, I ask you to take an unusual action inside the open source community. Donate the money to a non-profit organization like Doctors Without Borders or the Children's Cancer Aid. I will continue to build tools because I like it and it is my passion to develop and share applications.

## License
This product is available under the Apache 2.0 license.