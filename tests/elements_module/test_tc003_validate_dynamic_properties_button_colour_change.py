import logging
import pytest

from lib.base_test import BaseTest

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver")
class TestDynamicProperties(BaseTest):
    """Dynamic Properties Test Class"""

    @pytest.mark.tc003
    def test_tc003_validate_dynamic_properties_button_color_change(self, driver):
        logger.info("----Start [TC_003] Verify Button Color Change ----")
        self.init_pages(driver)

        logger.info("[Step 1]: Navigate to Elements > Dynamic Properties section")
        self.home_page.remove_ads()
        self.home_page.move_to_elements_page()
        self.dynamic_properties_page.click_dynamic_properties_button()

        logger.info("[Step 2]: Get initial background color of the button")
        initial_color = self.dynamic_properties_page.get_color_change_button_color()
        logger.info(f"[Initial Color] {initial_color}")

        logger.info("[Step 3]: Wait for the button color to change")
        self.dynamic_properties_page.wait_for_color_change()

        logger.info("[Step 4]: Verify the color change")
        final_color = self.dynamic_properties_page.get_color_change_button_color()
        logger.info(f"[Final Color] {final_color}")
        assert initial_color != final_color, "Button color did not change."

        logger.info("[Expected Result] Button color changed.")
        logger.info("----End [TC_003]----")