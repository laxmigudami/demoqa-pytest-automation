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
- Configuration files for global settings (`pytest.ini`, `requirements.txt`)

## Pre-requisites

Ensure that you have the following installed:
- Python 3.x
- `pip` for managing dependencies
- Git (for version control)
  
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

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
## Running Tests

To run the tests, use the following command:

```bash
pytest
```

By default, tests will be executed with the following configurations:
- **HTML report generation**: The result will be saved in `reports/report.html`.
- **Screenshots**: Screenshots will be saved in `reports/screenshots/` in case of a test failure.

### Additional Pytest Options
- `--maxfail=1`: Fail the test run after the first failure.
- `--disable-warnings`: Disable warnings for a cleaner output.

## Directory Structure

```
demoqa-pytest-automation/
├── config/                  
│   ├── config.yaml           # Base URL and environment settings
│   └── user_data.json        # Test data for form inputs
├── lib/                     
│   ├── base_test.py          # Base test setup/teardown
│   └── utils.py              # Helper methods for tests
├── pages/                    # Page Object Model classes
│   └── *.py                  # Individual page modules
├── reports/                 
│   ├── report.html           # Pytest HTML report
│   └── screenshots/          # Failure screenshots
├── tests/                   
│   ├── test_tc001.py         # Test case 1
│   ├── test_tc002.py         # Test case 2
│   └── ...                   # More test cases
├── .gitignore                # Files to be ignored by Git
├── conftest.py               # Global fixtures and hooks
├── pytest.ini                # Pytest configuration (report, logs, markers)
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation

```

## Configuration

### `pytest.ini`

The `pytest.ini` file is used for global configuration of the Pytest framework, including logging and HTML report settings.

### `conftest.py`

The `conftest.py` file is used to configure test fixtures such as:
- WebDriver setup and teardown
- Screenshot capture on test failure
- Loading configuration and test data

## Troubleshooting

1. **Missing Dependencies**: Ensure that you have all dependencies installed by running `pip install -r requirements.txt`.
2. **Test Failures**: Check the HTML report or logs for more details on why a test failed. Screenshots will be available in the `reports/screenshots/` folder for failed tests.
