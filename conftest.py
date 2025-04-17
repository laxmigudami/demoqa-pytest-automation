import json
import os

import pytest
from selenium import webdriver
import yaml
from selenium.webdriver.chrome.options import Options
from datetime import datetime

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="class")
def driver(config):
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(config["base_url"])
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    yield
    outcome = request.node.rep_call
    if outcome.failed:
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{request.node.name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        driver.save_screenshot(filepath)
        print(f"\n[SCREENSHOT SAVED] {filepath}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture
def load_user_data():
    """Fixture to load user data from config/user_data.json"""
    path = os.path.join("config", "user_data.json")
    with open(path) as file:
        return json.load(file)
