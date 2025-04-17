from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.homepage import HomePage
from pages.checkbox_page import CheckboxPage
from pages.practiceform_page import PracticeFormPage
from pages.bookstore_page import BookStorePage

class BaseTest:
    """Base test class for all Tests."""

    def init_pages(self, driver):
        self.home_page = HomePage(driver)
        self.checkbox_page = CheckboxPage(driver)
        self.dynamic_properties_page = DynamicPropertiesPage(driver)
        self.practiceform_page = PracticeFormPage(driver)
        self.bookstore_page = BookStorePage(driver)


