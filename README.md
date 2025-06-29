# Python Dojo Katas

Welcome to the Python Dojo Katas project! This repository is designed to help you practice and enhance your skills in Python, focusing on Pydantic, PydanticAI, and UV frameworks. Each kata is structured to provide hands-on experience with various concepts and techniques.

## Project Structure

The project is organized as follows:

```
python-dojo-katas/
├── src/
│   └── python_dojo_katas/       # Main package
│       ├── pydantic_katas/      # Katas focused on Pydantic
│       │   ├── basic_models.py  # Basic Pydantic models
│       │   ├── validation_katas.py # Validation exercises
│       │   └── advanced_features.py # Advanced Pydantic features
│       ├── pydantic_ai_katas/   # Katas focused on PydanticAI
│       │   ├── basic_agents.py  # Basic agent implementations
│       │   ├── tool_integration.py # Tool integration with agents
│       │   └── streaming_katas.py # Streaming data exercises
│       └── uv_katas/            # Katas focused on UV
│           ├── dependency_management.py # Dependency management techniques
│           └── project_setup.py # UV project setup guidance
├── tests/                       # Unit tests for the katas
│   ├── test_pydantic_katas.py   # Tests for Pydantic katas
│   ├── test_pydantic_ai_katas.py # Tests for PydanticAI katas
│   └── test_uv_katas.py         # Tests for UV katas
├── pyproject.toml               # Project configuration and dependencies
└── uv.lock                      # Lock file for UV dependencies
```

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd python-dojo-katas
   ```

2. **Install UV (if not already installed):**
   UV is a fast Python package installer and resolver. Install it following the [official UV installation guide](https://docs.astral.sh/uv/getting-started/installation/), or use:

   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Set up the project environment:**
   UV will automatically create a virtual environment and install dependencies:

   ```bash
   uv sync
   ```

4. **Activate the virtual environment (optional):**
   While not required for running UV commands, you can activate the environment for direct Python usage:

   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

5. **Run Tests:**
   To ensure everything is working correctly and all katas are implemented properly:

   ```bash
   uv run pytest tests/ -v
   ```

   Or if you have the environment activated:

   ```bash
   pytest tests/ -v
   ```

6. **Explore the Katas:**
   Navigate to the `src/python_dojo_katas/` directory to find the katas for Pydantic, PydanticAI, and UV. Each kata is designed to help you practice specific concepts.

## What's Included

### Pydantic Katas

- **Basic Models**: Learn how to create and use Pydantic models with proper validation
- **Validation Katas**: Practice custom validation logic and error handling
- **Advanced Features**: Explore more sophisticated Pydantic capabilities

### PydanticAI Katas

- **Basic Agents**: Simple agent implementations with basic functionality
- **Tool Integration**: Learn how to integrate external tools with AI agents
- **Streaming Katas**: Handle streaming data in AI applications

### UV Katas

- **Dependency Management**: Practice managing Python dependencies with UV
- **Project Setup**: Learn UV project configuration and setup patterns

## Testing

The project includes comprehensive tests for all katas. All tests are currently passing and cover:

- **12 test cases** across three modules
- **Pydantic model validation** and error handling
- **AI agent functionality** and tool integration
- **UV dependency management** operations

Run the test suite to verify your implementations and practice test-driven development patterns.

## Development Workflow

### Running Individual Test Modules

You can run tests for specific kata modules:

```bash
# Test Pydantic katas only
uv run pytest tests/test_pydantic_katas.py -v

# Test PydanticAI katas only  
uv run pytest tests/test_pydantic_ai_katas.py -v

# Test UV katas only
uv run pytest tests/test_uv_katas.py -v
```

### Adding Dependencies

To add new dependencies to the project:

```bash
# Add runtime dependencies
uv add package-name

# Add development dependencies
uv add --dev package-name
```

### Code Quality Tools

The project includes several development tools configured in `pyproject.toml`:

- **Black**: Code formatting
- **Ruff**: Fast Python linter and formatter
- **MyPy**: Type checking
- **Pre-commit**: Git hooks for code quality

Run quality checks:

```bash
# Format code with Black
uv run black src/ tests/

# Lint with Ruff
uv run ruff check src/ tests/

# Type checking with MyPy
uv run mypy src/
```

## Contributing

Feel free to contribute to this project by adding new katas, improving existing ones, or enhancing documentation. Open an issue or submit a pull request for any changes you would like to propose.

Happy coding!
