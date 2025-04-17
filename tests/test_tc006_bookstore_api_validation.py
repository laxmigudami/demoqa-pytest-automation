import logging
import pytest
from lib.base_test import BaseTest
from lib.api_utils import get_books_from_api

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
class TestBookStore(BaseTest):
    """Book Store Data Validation"""

    @pytest.mark.tc006
    def test_tc006_validate_book_store_data(self, driver):
        logger.info("----Start [TC_006] Validate Book Store UI vs API----")
        self.init_pages(driver)

        logger.info("[Step 1]: Navigate to Book Store Application")
        self.home_page.remove_ads()
        self.home_page.move_to_book_store_app_page()
        self.bookstore_page.click_book_store()
        assert self.bookstore_page.is_book_store_view_displayed(), "Book Store is not displayed"

        logger.info("[Step 2]: Get books displayed in UI")
        ui_books = self.bookstore_page.get_ui_books()

        logger.info("[Step 3]: Get books from API")
        api_books = get_books_from_api()

        logger.info("[Step 4]: Validate UI and API book lists match")
        assert sorted(ui_books) == sorted(api_books), f"Book list mismatch!\nUI: {ui_books}\nAPI: {api_books}"

        logger.info("[Expected Result]: Book titles from UI should match with API data")
        logger.info("----End [TC_006]----")