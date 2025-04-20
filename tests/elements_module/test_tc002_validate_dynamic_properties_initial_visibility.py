import logging

import pytest

from lib.base_test import BaseTest

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver")
class TestDynamicProperties(BaseTest):
    """Dynamic Properties Test Class"""

    @pytest.mark.tc002
    def test_tc002_validate_dynamic_properties_initial_visibility(self, driver):
        logger.info("----Start [TC_002] Verify Dynamic Properties initial visibility ----")
        self.init_pages(driver)

        logger.info("[Step 1]: Navigate to Elements > Dynamic Properties section")
        self.home_page.remove_ads()
        self.home_page.move_to_elements_page()
        self.dynamic_properties_page.click_dynamic_properties_button()

        logger.info("[Step 2]: Verify 'Dynamic Properties' page header is displayed")
        assert self.dynamic_properties_page.is_dynamic_properties_header_displayed(), (
            "Dynamic Properties header not displayed"
        )
        header_text = self.dynamic_properties_page.get_dynamic_properties_header_text()
        assert "Dynamic Properties" in header_text, "Unexpected header text"
        logger.info(f"[Expected Result] Header text is: '{header_text}'")

        logger.info("[Step 3]: Verify 'Will enable 5 seconds' button is displayed before 5 seconds")
        assert self.dynamic_properties_page.is_enable_after_button_displayed(), (
            "'Enable after 5 seconds' button not displayed initially"
        )

        logger.info("[Step 4]: Wait for 'Visible after 5 seconds' button to appear")
        self.dynamic_properties_page.wait_for_visible_after_button()

        logger.info("[Step 5]: Assert the button is visible after delay")
        assert self.dynamic_properties_page.is_visible_after_button_displayed(), (
            "'Visible after 5 seconds' button is not visible after 5 seconds"
        )

        logger.info("[Expected Result] 'Visible after 5 seconds' button is now visible.")
        logger.info("----End [TC_002]----")
