import unittest
from src.python_dojo_katas.uv_katas.dependency_management import manage_dependencies
from src.python_dojo_katas.uv_katas.project_setup import setup_uv_project

class TestUVKatas(unittest.TestCase):

    def test_manage_dependencies(self):
        # The function expects dependencies in format "name==version"
        dependencies = ["requests==2.28.0", "pydantic==2.0.0"]
        result = manage_dependencies(dependencies)
        self.assertIsInstance(result, dict)  
        self.assertEqual(result["requests"], "2.28.0")
        self.assertEqual(result["pydantic"], "2.0.0")

    def test_initialize_project(self):
        # setup_uv_project doesn't take parameters and doesn't return anything
        # We'll just test that it can be called without error
        try:
            setup_uv_project()
            result = True  # If no exception, consider success
        except Exception:
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()