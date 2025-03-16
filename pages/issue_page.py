import time

from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from utils.logger import get_logger
from utils.object_repository import get_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IssuesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger()

    def create_issue(self, issue_title, label=None, assignee=None):
        """Creates a new issue with optional label and assignee."""
        try:
            self.find_element("new_issue_button").click()
            self.find_element("issue_title_input").send_keys(issue_title)

            # Assign Label if provided
            if label:
                self.find_element("label_filter_section").click()
                time.sleep(1)
                label_input = self.find_element("label_filter_text")  # Find search input for labels
                label_input.send_keys(label)
                label_input.send_keys(Keys.RETURN)  # Press Enter to select
                self.logger.info(f"Label '{label}' selected.")

            # Assign Assignee if provided
            if assignee:
                self.find_element("assignee_filter_section").click()
                time.sleep(1)
                assignee_input = self.find_element("assignee_filter_text")  # Find input box
                assignee_input.send_keys(assignee)
                assignee_input.send_keys(Keys.RETURN)  # Press Enter to select
                self.logger.info(f"Assignee '{assignee}' selected.")

            # Submit the issue
            self.find_element("submit_issue_button").click()
            self.logger.info(f"Issue '{issue_title}' created successfully.")
            return f"Issue '{issue_title}' created successfully."

        except NoSuchElementException as e:
            self.logger.error(f"Error creating issue: {str(e)}")
            return f"Error creating issue: {str(e)}"

    # def verify_issue_exists(self, issue_title):
    #     """Checks if an issue with the given title exists in the issue list."""
    #     try:
    #         issue_list = self.find_elements("issue_titles")  # Get all issue titles on the page
    #         for issue in issue_list:
    #             if issue.text.strip() == issue_title:
    #                 self.logger.info(f"Issue '{issue_title}' is listed successfully.")
    #                 return True
    #         self.logger.error(f"Issue '{issue_title}' not found in the list.")
    #         return False
    #     except NoSuchElementException:
    #         self.logger.error("Error: Unable to locate issue list.")
    #         return False

    def verify_issue_exists(self, issue_title):
        """Checks if an issue with the given title exists in the issue list."""
        try:
            time.sleep(2)
            self.find_element("issues_tab").click()
            time.sleep(3)
            issue_elements = self.find_elements("issue_titles")  # Get list of issue elements

            if not issue_elements:
                self.logger.error("No issues found! Check the XPath.")
                assert False, "❌ Issue list is empty. Issue might not have been created!"

            issue_list = [issue.text.strip() for issue in issue_elements if issue.text.strip()]
            self.logger.info(f"Extracted Issues: {issue_list}")

            if issue_title in issue_list:
                self.logger.info(f"✅ Issue '{issue_title}' is listed successfully.")
                return True
            else:
                self.logger.error(f"❌ Issue '{issue_title}' NOT found in the issue list!")
                assert False, f"Issue '{issue_title}' was NOT found in the repository issue list!"

        except NoSuchElementException:
            self.logger.error("❌ Error: Unable to locate issue list.")
            assert False, "Unable to locate issue list on the GitHub UI!"

    def verify_notification_received(self):
        """Checks if a GitHub notification is received after issue creation."""
        try:
            notification_icon = self.find_element("notification_icon")  # Locate the notification icon
            notification_count = notification_icon.text.strip()

            if notification_count and int(notification_count) > 0:
                self.logger.info(f"Notification received! Count: {notification_count}")
                return True
            else:
                self.logger.warning("No new notification received.")
                return False

        except NoSuchElementException:
            self.logger.error("Error: Notification icon not found.")
            return False


