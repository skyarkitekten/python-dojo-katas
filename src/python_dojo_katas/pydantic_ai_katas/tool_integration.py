from typing import Any, Dict
import requests


def integrate_tool_with_agent(
    agent: Any, tool_name: str, tool_config: Dict[str, Any]
) -> None:
    """
    Integrates a specified tool with a Pydantic agent.

    Args:
        agent: The Pydantic agent instance to integrate with the tool.
        tool_name (str): The name of the tool to integrate.
        tool_config (Dict[str, Any]): Configuration parameters for the tool.

    Raises:
        ValueError: If the tool name is not recognized.
    """
    if tool_name == "example_tool":
        # Example integration logic
        response = requests.post(tool_config["url"], json=agent.dict())
        if response.status_code != 200:
            raise ValueError("Failed to integrate with the tool.")
    else:
        raise ValueError(f"Tool '{tool_name}' is not recognized.")


def fetch_tool_data(tool_name: str) -> Dict[str, Any]:
    """
    Fetches data from an external tool.

    Args:
        tool_name (str): The name of the tool to fetch data from.

    Returns:
        Dict[str, Any]: The data retrieved from the tool.

    Raises:
        ValueError: If the tool name is not recognized or data fetching fails.
    """
    if tool_name == "example_tool":
        response = requests.get("https://api.example.com/data")
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to fetch data from the tool.")
    else:
        raise ValueError(f"Tool '{tool_name}' is not recognized.")
