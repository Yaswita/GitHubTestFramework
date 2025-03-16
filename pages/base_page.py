import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.object_repository import get_object

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, variable):
        """ Fetch XPath using get_object() and locate the element """
        xpath = get_object(variable)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def launch_application(self, url):
        """ Open the GitHub URL """
        self.driver.get(url)

    def is_text_present(self, text):
        """Check if a given text is present anywhere on the page."""
        return text in self.driver.page_source

    def navigate_to(self, url):
        """Navigates to the given URL."""
        self.driver.get(url)
        time.sleep(1)
        # Handle multiple windows if any
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the latest window

    def find_element_by_text(self, text):
        """Find an element based on its text content."""
        xpath = f"//*[contains(text(), '{text}')]"
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_elements(self, param):
        """ Fetch XPath using get_object() and locate all matching elements """
        xpath = get_object(param)
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

    def is_element_present(self, xpath):
        """Check if an element is present on the page without throwing an exception."""
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return True
        except:
            return False

    def delete_repo(self):
        self.find_element("settings_xpath").click()
        time.sleep(1)
        self.find_element("delete_repo_xpath").click()
        time.sleep(1)
        self.find_element("i_want_to_xpath").click()
        time.sleep(1)
        self.find_element("i_have_read_xpath").click()
        time.sleep(1)
        value = self.find_element("verification_xpath").get_attribute("data-repo-nwo")
        time.sleep(1)
        self.find_element("verification_xpath").send_keys(value)
        time.sleep(1)
        self.find_element("delete_proceed_xpath").click()
