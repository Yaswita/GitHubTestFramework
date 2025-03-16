import time

from pages.base_page import BasePage
from utils.logger import get_logger
from selenium.common.exceptions import NoSuchElementException


class RepositoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger()

    def create_repository(self, repo_name, is_private=False):
        """Creates a new repository with the specified name and visibility."""
        try:
            self.find_element("new_repo_button").click()
            time.sleep(2)
            self.find_element("repo_name_input").send_keys(repo_name)

            if is_private:
                self.find_element("private_repo_option").click()
            else:
                self.find_element("public_repo_option").click()
            time.sleep(2)
            self.find_element("create_repo_button").click()
            self.logger.info(f"Repository '{repo_name}' created successfully.")
            return f"Repository '{repo_name}' created successfully."

        except NoSuchElementException as e:
            self.logger.error(f"Error creating repository: {str(e)}")
            return f"Error creating repository: {str(e)}"

    def verify_repository_details(self, expected_repo_name, expected_visibility):
        """Validates repository name and visibility settings."""
        try:
            repo_name_element = self.find_element("repo_name_xpath")
            visibility_element = self.find_element("label_xpath")  # Holds the visibility (public/private)

            actual_repo_name = repo_name_element.text.strip()
            actual_visibility = visibility_element.text.strip().lower()

            # Validate repository name
            if actual_repo_name != expected_repo_name:
                error_msg = f"Error: Expected repo name '{expected_repo_name}', but found '{actual_repo_name}'"
                self.logger.error(error_msg)
                return False, error_msg

            # Validate repository visibility
            if "public" in actual_visibility:
                actual_visibility = "public"
            elif "private" in actual_visibility:
                actual_visibility = "private"
            else:
                self.logger.error("Error: Unable to determine repository visibility.")
                return False, "Error: Unable to determine repository visibility."

            if actual_visibility != expected_visibility.lower():
                error_msg = f"Error: Expected visibility '{expected_visibility}', but found '{actual_visibility}'"
                self.logger.error(error_msg)
                return False, error_msg

            success_msg = "Repository details verified successfully."
            self.logger.info(success_msg)
            return True, success_msg

        except NoSuchElementException as e:
            error_msg = f"Error verifying repository details: {str(e)}"
            self.logger.error(error_msg)
            return False, error_msg

    def is_repository_present(self, repo_name):
        """Checks if a repository with the given name exists."""
        time.sleep(2)
        self.navigate_to("https://github.com/yaswitabalu87?tab=repositories")
        time.sleep(2)
        try:
            repo_element = self.find_element_by_text(repo_name)
            return repo_element is not None
        except NoSuchElementException:
            return False

    def navigate_to_repository(self, repo_name):
        """Navigates to a specific repository."""
        self.find_element_by_text(repo_name).click()

    def navigate_to_issues(self):
        """Navigates to the Issues tab inside a repository."""
        self.find_element("issues_tab").click()