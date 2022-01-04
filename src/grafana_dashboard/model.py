class Model:
    """The class describes and set up all necessary values for the template mechanism as a data model.

    Keyword arguments:
    dashboard_templates_path -> Specify the template path for all dashboard's
    dashboard_type -> Specify the dashboard type e.g. database
    dashboard_name -> Specify the dashboard name e.g. postgres
    dashboard_version -> Specify the dashboard version e.g. v13
    """

    def __init__(
        self,
        dashboard_templates_path: str = None,
        dashboard_type: str = None,
        dashboard_name: str = None,
        dashboard_version: str = None,
    ):
        self.dashboard_templates_path = dashboard_templates_path
        self.dashboard_type = dashboard_type
        self.dashboard_name = dashboard_name
        self.dashboard_version = dashboard_version
