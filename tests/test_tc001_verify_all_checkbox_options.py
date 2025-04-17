import logging
import pytest
from lib.base_test import BaseTest
logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
class TestCheckbox(BaseTest):

    @pytest.mark.tc001
    def test_tc1_checkbox_expand_and_select(self, driver):

        logger.info("----Start [TC_001] Checkbox Expand and Select Test ----")
        logger.info("[Step 1]: Navigate to Check Box from Home Page")
        self.init_pages(driver)
        self.home_page.remove_ads()
        self.home_page.move_to_elements_page()
        assert self.home_page.is_select_page_view_displayed(), "Elements page view not displayed"

        logger.info("[Step 2] Navigate to Check Box section under Elements")
        self.checkbox_page.click_check_box()
        assert self.checkbox_page.is_check_box_center_displayed(), "Check Box section not displayed"

        logger.info("[Step 3] Expand all parent nodes dynamically")
        self.checkbox_page.expand_all_collapsed_nodes()
        assert self.checkbox_page.get_collapsed_nodes_count() == 3, "Expected 3 collapsed nodes"

        logger.info("[Step 4] Expand 'Desktop' node and verify nested elements")
        self.checkbox_page.expand_desktop_node()
        nested_elements = self.checkbox_page.get_desktop_node_children()
        expected_labels = ["Notes", "Commands"]
        actual_labels = [el.text for el in nested_elements]
        for label in expected_labels:
            assert label in actual_labels, f"Expected child label '{label}' not found"
        logger.info("[Expected Result] Nested 'Notes' and 'Commands' elements are present under 'Desktop'")
        logger.info("----End [TC_001]----")
