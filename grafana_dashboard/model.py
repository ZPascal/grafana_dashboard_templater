class Model:
    """The class includes all necessary variables to specify a query for the datasource search endpoint

    Args:
        dashboard_templates_path (str): Specify the template path for all dashboard's (default None)
        dashboard_type (str): Specify the dashboard type e.g. database (default None)
        dashboard_name (str): Specify the dashboard name e.g. postgres (default None)
        dashboard_version (str): Specify the dashboard version e.g. v13 (default None)
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
