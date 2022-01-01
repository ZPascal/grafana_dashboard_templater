class Model:
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
