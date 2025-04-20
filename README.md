
## Welcome!!!
# DemoQA Pytest Automation Framework

This is a Pytest-based automation framework built using Selenium for web testing. The framework follows the Page Object Model (POM) design pattern and includes test scenarios for the DemoQA website, which provides an interactive platform for automating different UI elements.

The framework includes configurations for global settings, a dependency management system (`requirements.txt`), and generates detailed HTML reports after every test run. It also includes logging and screenshot capture functionality for failed test cases.

## Features
- Pytest-based automation framework
- Selenium WebDriver for browser automation
- Page Object Model (POM) design pattern
- Test scenarios for DemoQA elements:
  - Checkbox
  - Dynamic Properties
  - Practice Forms
  - Book Store Application (UI and API validation)
- Test data handling through JSON configuration files
- HTML reports with `pytest-html` plugin
- Logs and screenshots for failed tests
- Configuration files for global settings (`pytest.ini`, `pyproject.toml`, `requirements.txt`)
- Static code analysis and formatting using `ruff`
- Dependency management with `pip-tools`

## Pre-requisites

Ensure that you have the following installed globally on your system:

- Python 3.x (recommended: Python 3.11+)
- `pip` (Python package manager)
- Git (for version control)

> 💡 All Python packages including **Selenium** will be automatically installed via `make requirements`.

  
## Installation

Follow these steps to install and set up the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/laxmigudami/demoqa-pytest-automation.git
   cd demoqa-pytest-automation
   ```

2. **Create a virtual environment:**
   For macOS/Linux:
   ```bash
   python3 -m venv .venv
   ```
   For Windows:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   For macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   For Windows:
   ```bash
   .\.venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   make requirements
   ```

   > This will compile `requirements.txt` from `requirements.in` using `pip-compile` and install them.

## Running Tests

To run the tests:

```bash
pytest
```

Test configuration includes:
- **HTML Report**: Output in `reports/report.html`
- **Screenshots**: Stored in `reports/screenshots/` for any test failures

### Additional Pytest Options
- `--maxfail=1`: Stop after first failure
- `--disable-warnings`: Suppress warnings

## Static Code Analysis

To run formatting and linting using [Ruff](https://docs.astral.sh/ruff/):

```bash
make sca
```

This will:
- Format code using `ruff format`
- Check for lint errors using `ruff check`

## Directory Structure

```
demoqa-pytest-automation/
├── config/                  
│   ├── config.yaml
│   └── user_data.json
├── lib/
│   ├── base_test.py
│   └── utils.py
├── pages/
│   └── *.py
├── reports/
│   ├── report.html
│   └── screenshots/
├── tests/
│   ├── elements_module/
│   ├── forms_module/
│   └── bookstore_module/
├── .gitignore
├── conftest.py
├── pytest.ini
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── Makefile
└── README.md
```

## Configuration

### `pytest.ini`
Configures logging, HTML reports, and test markers.

### `conftest.py`
Sets up fixtures:
- WebDriver lifecycle
- Screenshot on failure
- Config and test data loading

### `pyproject.toml`
Configures `ruff` for code formatting and linting.

## Troubleshooting

- **Dependency Errors**: Run `make requirements` to ensure all dependencies are resolved.
- **Linting Errors**: Run `make sca` and follow suggestions to fix errors.
- **Test Failures**: Check HTML report and screenshots for failure context.
```