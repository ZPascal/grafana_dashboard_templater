import os
import sys
import json
import logging
from typing import Dict
import tempfile

import jinja2

from .model import Model


class Dashboard:
    """The class includes all necessary methods to template the selected dashboard and return it as a dict

    Args:
        dashboard_model (Model): Inject a dashboard object that includes all necessary values and information

    Attributes:
        dashboard_model (Model): This is where we store the model
        logging (logging.Logger): This is where we store the logger
    """

    def __init__(self, dashboard_model: Model):
        self.dashboard_model = dashboard_model
        self.logging = logging.Logger

    def get_dashboard_json(self, template_values: Dict) -> Dict:
        """The method includes a functionality to template the selected dashboard and return the corresponding dashboard as dictionary

        Args:
            template_values (Dict): Specify the inserted templating values as dict

        Raises:
            jinja2.TemplateNotFound: Jinja2 template not found

        Returns:
            json_dashboard (Dict): Returns the dashboard as dict
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

        with tempfile.NamedTemporaryFile() as tmp_file:
            self.__write_tmp_dashboard_json(
                tmp_file.name, template_dashboard, template_values
            )
            return self.__get_dashboard_json(tmp_file.name)

    @staticmethod
    def __write_tmp_dashboard_json(
        temp_path: str, template_dashboard: jinja2.Template, template_values: Dict
    ):
        """The method includes a functionality to write a templated json of the selected dashboard to a temporary file

        Args:
            temp_path (str): Specify the temporary path as string
            template_dashboard (jinja2.Template): Specify the Jinja2 templated dashboard
            template_values (Dict): Specify the template values

        Raises:
            FileNotFoundError: The corresponding temporary file is not available
            ValueError: There is an error inside the values
            AttributeError: You missed to add a specific attribute

        Returns:
            None
        """

        try:
            fw = open(temp_path, "w")
            fw.write(template_dashboard.render(template_values))
            fw.close()
        except (FileNotFoundError, ValueError, AttributeError) as e:
            logging.error(f"Please, check the error: {e} .")
            raise e

    @staticmethod
    def __get_dashboard_json(temp_path: str) -> Dict:
        """The method includes a functionality to get the corresponding templated dashboard JSON as Dict

        Args:
            temp_path (str): Specify the temporary path as string

        Raises:
            FileNotFoundError: The corresponding temporary file is not available
            ValueError: There is an error inside the values

        Returns:
            json_dashboard (Dict): Returns the dashboard JSON as dict
        """

        try:
            with open(temp_path) as file:
                json_dashboard: Dict = json.load(file)
        except (FileNotFoundError, ValueError) as e:
            logging.error(f"Please, check the error: {e} .")
            raise e

        return json_dashboard

    def __get_dashboard_template(self) -> str:
        """The methode identify and return the path of the dashboard template sample

        Returns:
            full_dashboard_path (str): Returns the full dashboard path
        """

        full_dashboard_path: str = (
            f"{self.dashboard_model.dashboard_templates_path}{os.sep}"
            f"{self.dashboard_model.dashboard_type}{os.sep}"
            f"{self.dashboard_model.dashboard_name}{os.sep}"
            f"{self.dashboard_model.dashboard_version}{os.sep}dashboard.json.sample"
        )

        return full_dashboard_path
