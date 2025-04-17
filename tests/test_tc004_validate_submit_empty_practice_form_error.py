import logging
import pytest
from lib.base_test import BaseTest

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
class TestPracticeForm(BaseTest):
    """Form Validation Tests"""

    @pytest.mark.tc004
    def test_tc004_validate_empty_form_submission_error(self, driver):
        logger.info("----Start [TC_004] Verify validation on empty form submission ----")
        self.init_pages(driver)

        logger.info("[Step 1]: Navigate to Forms > Practice Forms section")
        self.home_page.remove_ads()
        self.home_page.move_to_forms_page()
        self.practiceform_page.click_practice_form()
        assert self.practiceform_page.is_form_header_displayed(), "Form header not displayed"

        logger.info("[Step 2]: Submit form without filling any fields")
        self.practiceform_page.click_submit()

        logger.info("[Step 3]: Verify validation for required fields")
        assert self.practiceform_page.is_validation_error_displayed("firstName"), "First Name field validation failed"
        assert self.practiceform_page.is_validation_error_displayed("lastName"), "Last Name field validation failed"
        assert self.practiceform_page.is_validation_error_displayed("userEmail"), "Email field validation failed"
        assert self.practiceform_page.is_validation_error_displayed("userNumber"), "Mobile Number field validation failed"

        logger.info("[Expected Result] All required fields should show validation errors")
        logger.info("----End [TC_004]----")
