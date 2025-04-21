import json
import os
from datetime import datetime

import pytest
import yaml
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)


def get_browser_options(browser_name, headless):
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return options
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return options
    elif browser_name == "ie":
        options = IEOptions()
        if headless:
            options.add_argument("--headless")
        return options
    elif browser_name == "safari":
        options = SafariOptions()
        if headless:
            options.add_argument("--headless")
        return options
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


@pytest.fixture(scope="class", params=["chrome"])  # Only using Chrome for now
def driver(request, config):
    browser = request.param
    headless = config["headless"]
    implicit_wait = config["implicit_wait"]

    options = get_browser_options(browser, headless)

    try:
        if browser == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox(options=options)
        elif browser == "ie":
            driver = webdriver.Ie(options=options)
        elif browser == "safari":
            driver = webdriver.Safari(options=options)

        driver.maximize_window()
        driver.implicitly_wait(implicit_wait)
        driver.get(config["base_url"])
        yield driver
        driver.quit()
    except SessionNotCreatedException as e:
        if "Safari" in str(e):
            pytest.skip("Safari WebDriver requires enabling 'Allow Remote Automation' in Safari's Develop menu")
        raise e


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
