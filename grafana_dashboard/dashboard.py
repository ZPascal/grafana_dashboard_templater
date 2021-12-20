import os
import sys
import json
import logging

import jinja2


class DashboardModel:

    def __init__(self, dashboard_templates_path: str = None, dashboard_type: str = None, dashboard_name: str = None,
                 dashboard_version: str = None, app_name: str = None, prometheus_name: str = None):
        self.dashboard_templates_path = dashboard_templates_path
        self.dashboard_type = dashboard_type
        self.dashboard_name = dashboard_name
        self.dashboard_version = dashboard_version
        self.app_name = app_name
        self.prometheus_name = prometheus_name


class Dashboard:
    def __init__(self, dashboard_model: DashboardModel):
        self.dashboard_model = dashboard_model
        self.logging = logging.Logger

    def get_dashboard_json(self):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("/"))

        try:
            logging.info("Load the PostgreSQL monitoring config template.")
            template_dashboard = env.get_template(Dashboard.__get_dashboard_template(self))
        except jinja2.TemplateNotFound as e:
            logging.error(f"Can not find the config template. Check the error: {e}.")
            sys.exit(1)

        if len(self.dashboard_model.prometheus_name) != 0:
            prometheus_name = self.dashboard_model.prometheus_name
        else:
            prometheus_name = self.dashboard_model.app_name

        dictionary_dashboard: dict = {
            "app_name": self.dashboard_model.app_name,
            "prometheus_name": prometheus_name
        }

        temp_path: str = "/tmp/dashboard.json"

        try:
            fw = open(temp_path, "w")
            fw.write(template_dashboard.render(dictionary_dashboard))
            fw.close()
        except jinja2.TemplateError as e:
            logging.error(f"Please, check the error: {e}.")
            sys.exit(1)

        try:
            with open(temp_path) as file:
                json_dashboard = json.load(file)
        except Exception as e:
            logging.error(f"Please, check the error: {e}")
            sys.exit(1)

        try:
            os.remove(temp_path)
        except Exception as e:
            logging.error(f"Please, check the error: {e}")
            sys.exit(1)

        return json_dashboard

    def __get_dashboard_template(self) -> str:
        full_dashboard_path: str = f"{self.dashboard_model.dashboard_templates_path}{os.sep}" \
                                   f"{self.dashboard_model.dashboard_type}{os.sep}" \
                                   f"{self.dashboard_model.dashboard_name}{os.sep}" \
                                   f"{self.dashboard_model.dashboard_version}{os.sep}dashboard.json.sample"
        return full_dashboard_path
