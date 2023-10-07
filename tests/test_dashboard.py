import logging
import os
import tempfile
from unittest import TestCase
from unittest.mock import MagicMock
import jinja2

from grafana_dashboard.model import Model
from grafana_dashboard.dashboard import Dashboard


class DashboardTestCase(TestCase):
    @staticmethod
    def __get_path_name() -> str:
        if os.path.basename(os.getcwd()) == "tests":
            return f"{os.path.dirname(os.getcwd())}{os.sep}dashboard-templates"
        else:
            return f"{os.getcwd()}{os.sep}dashboard-templates"

    def test_dashboard_successful(self):
        test_model: Model = Model("test1", "test2", "test3", "test4")
        test_dashboard: Dashboard = Dashboard(test_model)

        self.assertEqual(
            "test1", test_dashboard.dashboard_model.dashboard_templates_path
        )
        self.assertEqual("test2", test_dashboard.dashboard_model.dashboard_type)
        self.assertEqual("test3", test_dashboard.dashboard_model.dashboard_name)
        self.assertEqual("test4", test_dashboard.dashboard_model.dashboard_version)
        self.assertEqual(logging.Logger, test_dashboard.logging)

    def test_dashboard_error(self):
        test_model: Model = Model("test12", "test22", "test32", "test42")
        test_dashboard: Dashboard = Dashboard(test_model)

        self.assertNotEqual(
            "test1", test_dashboard.dashboard_model.dashboard_templates_path
        )
        self.assertNotEqual("test2", test_dashboard.dashboard_model.dashboard_type)
        self.assertNotEqual("test3", test_dashboard.dashboard_model.dashboard_name)
        self.assertNotEqual("test4", test_dashboard.dashboard_model.dashboard_version)
        self.assertNotEqual("Test", test_dashboard.logging)

    def test_get_dashboard_json_successful(self):
        template_path: str = DashboardTestCase.__get_path_name()
        test_model: Model = Model(template_path, "database", "postgresql", "v13")
        test_dashboard: Dashboard = Dashboard(test_model)
        dashboard = test_dashboard.get_dashboard_json(
            {"app_name": "test", "prometheus_name": "test_name-postgresql"}
        )

        self.assertEqual("Performance metrics for Postgres", dashboard["description"])
        self.assertEqual(
            'label_values(up{job="test_name-postgresql"},instance)',
            dashboard["templating"]["list"][0]["definition"],
        )
        self.assertEqual("Test Postgresql", dashboard["title"])

    def test_get_dashboard_json_no_config_template_error(self):
        template_path: str = f"{os.path.dirname(os.getcwd())}{os.sep}dashboard"
        test_model: Model = Model(template_path, "database", "postgresql", "v13")
        test_dashboard: Dashboard = Dashboard(test_model)
        with self.assertRaises(jinja2.TemplateNotFound):
            test_dashboard.get_dashboard_json(
                {"app_name": "test", "prometheus_name": "test_name"}
            )

    def test_get_dashboard_json_no_template_values_error(self):
        template_path: str = DashboardTestCase.__get_path_name()
        test_model: Model = Model(template_path, "database", "postgresql", "v13")
        test_dashboard: Dashboard = Dashboard(test_model)

        with self.assertRaises(SystemExit):
            test_dashboard.get_dashboard_json({})

    def test__write_tmp_dashboard_json_write_not_possible(self):
        template_path: str = DashboardTestCase.__get_path_name()
        test_model: Model = Model(template_path, "database", "postgresql", "v13")
        test_dashboard: Dashboard = Dashboard(test_model)

        with self.assertRaises(AttributeError):
            with tempfile.NamedTemporaryFile() as tmp_file:
                test_dashboard._Dashboard__write_tmp_dashboard_json(
                    tmp_file.name,
                    MagicMock,
                    {"app_name": "test", "prometheus_name": "test_name"},
                )

    def test__get_dashboard_json_json_not_available(self):
        template_path: str = DashboardTestCase.__get_path_name()
        test_model: Model = Model(template_path, "database", "postgresql", "v13")
        test_dashboard: Dashboard = Dashboard(test_model)

        with self.assertRaises(FileNotFoundError):
            test_dashboard._Dashboard__get_dashboard_json("/tmp/dashboard1.json")
