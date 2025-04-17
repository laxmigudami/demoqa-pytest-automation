import logging
import pytest
from lib.base_test import BaseTest

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver")
class TestPracticeForm(BaseTest):
    """Practice Form Submission Tests"""

    @pytest.mark.tc005
    def test_tc005_validate_submission_of_practice_form_with_data(
        self, driver, load_user_data
    ):
        logger.info("----Start [TC_005] Validate form submission with valid data ----")
        self.init_pages(driver)

        logger.info("[Step 1]: Navigate to Forms > Practice Forms section")
        self.home_page.remove_ads()
        self.home_page.move_to_forms_page()
        self.practiceform_page.click_practice_form()
        assert self.practiceform_page.is_form_header_displayed(), "Form header not displayed"

        logger.info("[Step 2]: Fill out the form with valid user data")
        self.practiceform_page.fill_form(
            first_name=load_user_data["first_name"],
            last_name=load_user_data["last_name"],
            email=load_user_data["email"],
            gender=load_user_data["gender"],
            mobile_number=load_user_data["mobile"]
        )

        logger.info("[Step 3]: Submit the form")
        self.practiceform_page.click_submit()

        logger.info("[Step 4]: Verify successful form submission")
        assert self.practiceform_page.is_submission_successful(), "Form submission failed"

        logger.info("[Expected Result] Form submitted successfully with confirmation modal")
        logger.info("----End [TC_005]----")
