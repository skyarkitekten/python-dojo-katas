from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from .config import settings

if not settings.model_name:
    raise ValueError("MODEL_NAME environment variable is required")

if not settings.openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

provider = OpenAIProvider(api_key=settings.openai_api_key)
model = OpenAIModel(provider=provider, model_name=settings.model_name)

# Create agent with validated settings
agent = Agent(
    model=model,
    system_prompt=settings.system_prompt or "You are a helpful assistant.",
)

result = agent.run_sync('Where is the Eiffel Tower located?')
print(result)
# Output: The Eiffel Tower is located in Paris, France.

result2 = agent.run_sync('Where does "hello, world" come from?')
print(result2)
# Output: "Hello, World!" is a phrase often used as a simple program example.