import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DynamicPropertiesPage:
    """Page Object for the Dynamic Properties section under Elements."""

    # Locators
    DYNAMIC_PROPERTIES_BUTTON = (
        By.CSS_SELECTOR,
        "div[class='element-list collapse show'] li[id='item-8']",
    )
    DYNAMIC_PROPERTIES_HEADER = (By.CSS_SELECTOR, "h1.text-center")
    VISIBLE_AFTER_BUTTON = (By.ID, "visibleAfter")
    ENABLE_AFTER_BUTTON = (By.ID, "enableAfter")
    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_dynamic_properties_button(self):
        """Click on the 'Dynamic Properties' section under Elements."""
        self.wait.until(EC.element_to_be_clickable(self.DYNAMIC_PROPERTIES_BUTTON)).click()

    def is_dynamic_properties_header_displayed(self):
        """Check if the page header 'Dynamic Properties' is displayed."""
        return self.driver.find_element(*self.DYNAMIC_PROPERTIES_HEADER).is_displayed()

    def get_dynamic_properties_header_text(self):
        """Get the text of the page header."""
        return self.driver.find_element(*self.DYNAMIC_PROPERTIES_HEADER).text

    def wait_for_visible_after_button(self):
        """Wait for the 'Visible after 5 seconds' button to appear."""
        self.wait.until(EC.visibility_of_element_located(self.VISIBLE_AFTER_BUTTON))

    def is_visible_after_button_displayed(self):
        """Check if the 'Visible after 5 seconds' button is displayed."""
        return self.driver.find_element(*self.VISIBLE_AFTER_BUTTON).is_displayed()

    def is_enable_after_button_displayed(self):
        """Check if the 'Will enable 5 seconds' button is displayed before it's enabled."""
        try:
            return self.driver.find_element(*self.ENABLE_AFTER_BUTTON).is_displayed()
        except Exception:
            return False

    def is_enable_after_button_enabled(self):
        """Check if the 'Will enable 5 seconds' button is enabled."""
        return self.driver.find_element(*self.ENABLE_AFTER_BUTTON).is_enabled()

    def wait_until_enable_after_button_is_enabled(self):
        """Wait until the 'Will enable 5 seconds' button becomes enabled."""
        self.wait.until(EC.element_to_be_clickable(self.ENABLE_AFTER_BUTTON))

    def get_color_change_button_color(self):
        """Get the current text color of the button."""
        button = self.driver.find_element(By.CSS_SELECTOR, "button#colorChange")
        return self.driver.execute_script("return window.getComputedStyle(arguments[0]).color;", button)

    def wait_for_color_change(self, timeout=10):
        """Wait until the button's background color changes."""
        initial_color = self.get_color_change_button_color()
        end_time = time.time() + timeout  # Set end time based on the timeout value

        while time.time() < end_time:
            current_color = self.get_color_change_button_color()
            if current_color != initial_color:
                return True  # Color has changed, return True
            time.sleep(0.5)  # Sleep for a short time before checking again

        return False  # If the color hasn't changed within the timeout, return False
