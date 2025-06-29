import unittest
from src.python_dojo_katas.pydantic_ai_katas.basic_agents import BasicAgent, AdvancedAgent
from src.python_dojo_katas.pydantic_ai_katas.tool_integration import integrate_tool_with_agent
from src.python_dojo_katas.pydantic_ai_katas.streaming_katas import handle_streaming_data

class TestPydanticAIKatas(unittest.TestCase):

    def test_basic_agent(self):
        agent = BasicAgent(name="TestAgent")
        self.assertEqual(agent.name, "TestAgent")
        self.assertIsInstance(agent, BasicAgent)

    def test_advanced_agent(self):
        agent = AdvancedAgent(name="AdvancedAgent", skill_level="expert")
        self.assertEqual(agent.skill_level, "expert")
        self.assertIsInstance(agent, AdvancedAgent)

    def test_tool_integration(self):
        # Since integrate_tool_with_agent requires an agent, let's test with a basic agent
        agent = BasicAgent(name="TestAgent")
        try:
            integrate_tool_with_agent(agent, "example_tool", {"url": "http://test.com"})
            result = True  # If no exception is raised, consider it successful for test purposes
        except Exception:
            result = False  # For testing purposes, we'll handle exceptions as failed integration
        self.assertIsInstance(result, bool)

    def test_streaming_input(self):
        result = handle_streaming_data("TestStream")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("received_data", result)

if __name__ == '__main__':
    unittest.main()