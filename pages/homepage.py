from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """Home page object"""

    ELEMENTS_CARD = (By.XPATH, '(//div[@class="card mt-4 top-card"])[1]')
    F0RMS_CARD = (By.XPATH, '(//div[@class="card mt-4 top-card"])[2]')
    BOOK_STORE_APPLICATION_CARD = (By.XPATH, '(//div[@class="card mt-4 top-card"])[6]')
    VIEW = (By.XPATH, "//div[@class='body-height']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def remove_ads(self):
        """Remove floating ads and popups that interfere with clicks."""
        self.driver.execute_script("""
            document.querySelectorAll(
                '#fixedban, .popup, .adsbygoogle, .google-auto-placed, [id*="google_vignette"]'
            ).forEach(el => el.remove());
        """)

    def move_to_elements_page(self):
        """Navigate to the 'Elements' card on the home page."""
        element = self.wait.until(EC.element_to_be_clickable(self.ELEMENTS_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_select_page_view_displayed(self):
        """Verify that the Select page is displayed after clicking."""
        return self.wait.until(EC.visibility_of_element_located(self.VIEW)).is_displayed()

    def move_to_forms_page(self):
        """Navigate to the 'Forms' card on the home page."""
        element = self.wait.until(EC.element_to_be_clickable(self.F0RMS_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def move_to_book_store_app_page(self):
        """Navigate to the Book Store Application card on the home page."""
        element = self.wait.until(EC.element_to_be_clickable(self.BOOK_STORE_APPLICATION_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
