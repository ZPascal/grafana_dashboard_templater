# Table of Contents

* [grafana\_dashboard.model](#grafana_dashboard.model)
  * [Model](#grafana_dashboard.model.Model)

<a id="grafana_dashboard.model"></a>

# grafana\_dashboard.model

<a id="grafana_dashboard.model.Model"></a>

## Model Objects

```python
class Model()
```

The class includes all necessary variables to specify a query for the datasource search endpoint

**Arguments**:

- `dashboard_templates_path` _str_ - Specify the template path for all dashboard's (default None)
- `dashboard_type` _str_ - Specify the dashboard type e.g. database (default None)
- `dashboard_name` _str_ - Specify the dashboard name e.g. postgres (default None)
- `dashboard_version` _str_ - Specify the dashboard version e.g. v13 (default None)

