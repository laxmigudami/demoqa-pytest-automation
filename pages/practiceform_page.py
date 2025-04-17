from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage
from selenium.webdriver.support.ui import WebDriverWait

class PracticeFormPage(HomePage):
    """Practice Form page object"""

    PRACTICE_FORM_BUTTON = (By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-0']")
    PRACTICE_FORM_TEXT = (By.CSS_SELECTOR, ".text-center")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userEmail")
    GENDER_RADIO_MALE = (By.XPATH, "//label[text()='Male']")
    GENDER_RADIO_FEMALE = (By.XPATH, "//label[text()='Female']")
    GENDER_RADIO_OTHER = (By.XPATH, "//label[text()='Other']")
    MOBILE_NUMBER_FIELD = (By.CSS_SELECTOR, "#userNumber")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    def __init__(self, driver):
        """Initialize the page object with driver and WebDriverWait"""
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def click_practice_form(self):
        """Click on the Practice Form from the sidebar menu."""
        self.wait.until(EC.element_to_be_clickable(self.PRACTICE_FORM_BUTTON)).click()

    def is_form_header_displayed(self):
        """Verify form header"""
        return self.wait.until(EC.visibility_of_element_located(self.PRACTICE_FORM_TEXT)).is_displayed()

    def fill_form(self, first_name, last_name, email, gender, mobile_number):
        """Fill out the form with provided data."""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.MOBILE_NUMBER_FIELD).send_keys(mobile_number)

        if gender.lower() == "male":
            self.driver.find_element(*self.GENDER_RADIO_MALE).click()
        elif gender.lower() == "female":
            self.driver.find_element(*self.GENDER_RADIO_FEMALE).click()
        else:
            self.driver.find_element(*self.GENDER_RADIO_OTHER).click()

    def click_submit(self):
        """Click the submit button."""
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.SUBMIT_BUTTON))

    def is_validation_error_displayed(self, field_id):
        """Check if a red border is applied to required fields."""
        field = self.driver.find_element(By.ID, field_id)
        return "field-error" in field.get_attribute("class") or field.get_attribute("value") == ""

    def is_submission_successful(self):
        """Check if the form submission was successful."""
        return "Thanks for submitting the form" in self.driver.page_source