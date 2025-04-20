from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.homepage import HomePage


class BookStorePage(HomePage):
    """Book Store page object"""

    BOOK_STORE_ELEMENT = (By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-2']")
    BOOK_LIST = (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
    BOOK_TITLE = (By.CSS_SELECTOR, ".rt-td:nth-child(2)")
    BOOK_STORE_VIEW = (By.CSS_SELECTOR, ".books-wrapper")

    def click_book_store(self):
        """Click on Book Store Application link"""
        self.wait.until(EC.element_to_be_clickable(self.BOOK_STORE_ELEMENT)).click()

    def get_ui_books(self):
        """Extract the list of book titles displayed in the UI"""
        books = []
        rows = self.driver.find_elements(*self.BOOK_LIST)
        for row in rows:
            title = row.find_element(*self.BOOK_TITLE).text.strip()
            if title:
                books.append(title)
        return books

    def is_book_store_view_displayed(self):
        """Check if the Book Store view is displayed."""
        return self.wait.until(EC.visibility_of_element_located(self.BOOK_STORE_VIEW)).is_displayed()
