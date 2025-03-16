from pages.base_page import BasePage
from utils.object_repository import get_object

class NavigationPage(BasePage):
    def navigate_to_issues(self):
        self.find_element("issues_tab").click()

    def navigate_to_pull_requests(self):
        self.find_element("pull_requests_tab").click()

    def click_tab(self, tab_name):
        """Click a tab using its name from object.ini."""
        self.find_element(tab_name).click()

    def is_tab_active(self, tab_name):
        """Check if the tab is active after clicking."""
        active_xpath = get_object(tab_name) + "[contains(@class, 'selected')]"
        return self.is_element_present(active_xpath)

    def check_pagination_exists(self):
        """Check if pagination exists on the page without failing the test."""
        return self.is_element_present(get_object("pagination_controls"))
