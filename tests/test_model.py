from unittest import TestCase

from grafana_dashboard.model import Model


class ModelTestCase(TestCase):
    def test_model_successful(self):
        test_model: Model = Model("test1", "test2", "test3", "test4")
        self.assertEqual("test1", test_model.dashboard_templates_path)
        self.assertEqual("test2", test_model.dashboard_type)
        self.assertEqual("test3", test_model.dashboard_name)
        self.assertEqual("test4", test_model.dashboard_version)

    def test_model_error(self):
        test_model: Model = Model("test12", "test22", "test32", "test42")
        self.assertNotEqual("test1", test_model.dashboard_name)
        self.assertNotEqual("test2", test_model.dashboard_type)
        self.assertNotEqual("test3", test_model.dashboard_version)
        self.assertNotEqual("test4", test_model.dashboard_templates_path)
