# Table of Contents

* [grafana\_dashboard.dashboard](#grafana_dashboard.dashboard)
  * [Dashboard](#grafana_dashboard.dashboard.Dashboard)
    * [get\_dashboard\_json](#grafana_dashboard.dashboard.Dashboard.get_dashboard_json)

<a id="grafana_dashboard.dashboard"></a>

# grafana\_dashboard.dashboard

<a id="grafana_dashboard.dashboard.Dashboard"></a>

## Dashboard Objects

```python
class Dashboard()
```

The class includes all necessary methods to template the selected dashboard and return it as a dict

**Arguments**:

- `dashboard_model` _Model_ - Inject a dashboard object that includes all necessary values and information
  

**Attributes**:

- `dashboard_model` _Model_ - This is where we store the model
- `logging` _logging.Logger_ - This is where we store the logger

<a id="grafana_dashboard.dashboard.Dashboard.get_dashboard_json"></a>

#### get\_dashboard\_json

```python
def get_dashboard_json(template_values: dict) -> dict
```

The method includes a functionality to template the selected dashboard and return the corresponding dashboard
as dictionary

**Arguments**:

- `template_values` _dict_ - Specify the inserted templating values as dict
  

**Raises**:

- `Exception` - Unspecified error by executing the functionality
  

**Returns**:

- `json_dashboard` _dict_ - Returns the dashboard as dict

