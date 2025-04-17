from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homepage import HomePage

class CheckboxPage(HomePage):
    """Check Box page object"""

    check_box_element = (By.XPATH, "//div[@class='element-list collapse show']//li[@id='item-1']")
    check_box_center = (By.CSS_SELECTOR, '.text-center')
    expand_toggle = (By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-close")
    collapsed_list = (By.XPATH, '//li[@class="rct-node rct-node-parent rct-node-collapsed"]')
    desktop_toggle = (By.XPATH, '(//button[@type="button" and @class="rct-collapse rct-collapse-btn"])[2]')
    desktop_list = (By.XPATH, "//li[@class='rct-node rct-node-parent rct-node-expanded']//ol/li[@class='rct-node rct-node-leaf']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_check_box(self):
        self.wait.until(EC.element_to_be_clickable(self.check_box_element)).click()

    def is_check_box_center_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.check_box_center)).is_displayed()

    def expand_all_collapsed_nodes(self):
        self.wait.until(EC.element_to_be_clickable(self.expand_toggle)).click()

    def get_collapsed_nodes_count(self):
        return len(self.driver.find_elements(*self.collapsed_list))

    def expand_desktop_node(self):
        self.wait.until(EC.element_to_be_clickable(self.desktop_toggle)).click()

    def get_desktop_node_children(self):
        return self.driver.find_elements(*self.desktop_list)