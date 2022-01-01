import os
import sys
import json
import logging

import jinja2

from src.grafana_dashboard.model import Model


class Dashboard:
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Keyword arguments:
    dashboard_model -> Inject a dashboard object that includes all necessary values and information
    """

    def __init__(self, dashboard_model: Model):
        self.dashboard_model = dashboard_model
        self.logging = logging.Logger

    def get_dashboard_json(self, template_values: dict) -> dict:
        """The method includes a functionality to template the selected dashboard and return the corresponding dashboard
           as dictionary

        Keyword arguments:
        template_values -> Specify the inserted templating values as dict
        """

        env = jinja2.Environment(loader=jinja2.FileSystemLoader("/"))

        try:
            logging.info("Load the config template.")
            template_dashboard = env.get_template(
                Dashboard.__get_dashboard_template(self)
            )
        except jinja2.TemplateNotFound as e:
            logging.error(f"Can not find the config template: {e} .")
            raise e

        if len(template_values) == 0:
            logging.error("Please define templating values.")
            sys.exit(1)

        temp_path: str = "/tmp/dashboard.json"

        try:
            fw = open(temp_path, "w")
            fw.write(template_dashboard.render(template_values))
            fw.close()
        except Exception as e:
            logging.error(f"Please, check the error: {e} .")
            raise e

        try:
            with open(temp_path) as file:
                json_dashboard = json.load(file)
        except Exception as e:
            logging.error(f"Please, check the error: {e} .")
            raise e

        try:
            os.remove(temp_path)
        except Exception as e:
            logging.error(f"Please, check the error: {e} .")
            raise e

        return json_dashboard

    def __get_dashboard_template(self) -> str:
        """The methode identify and return the path of the dashboard template sample"""
        full_dashboard_path: str = (
            f"{self.dashboard_model.dashboard_templates_path}{os.sep}"
            f"{self.dashboard_model.dashboard_type}{os.sep}"
            f"{self.dashboard_model.dashboard_name}{os.sep}"
            f"{self.dashboard_model.dashboard_version}{os.sep}dashboard.json.sample"
        )
        return full_dashboard_path
