from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.object_repository import get_object
from selenium.common.exceptions import StaleElementReferenceException
import time

class PullRequestPage(BasePage):
    # def create_branch(self, branch_name):
    #     """Creates a new branch from the main branch."""
    #     self.find_element("branch_selector").click()
    #     time.sleep(1)
    #     self.find_element("new_branch_input").send_keys(branch_name)
    #     self.find_element("new_branch_input").send_keys(Keys.RETURN)
    #     time.sleep(2)
    #     print(f"Branch '{branch_name}' created successfully.")
    #
    # def add_readme_file(self, content):
    #     """Adds a README file to the repository."""
    #     self.find_element("add_file_button").click()
    #     time.sleep(1)
    #     self.find_element("create_new_file_button").click()
    #     self.find_element("file_name_input").send_keys("README.md")
    #     self.find_element("file_content_input").send_keys(content)
    #     self.find_element("commit_changes_button").click()
    #     print("README file added successfully.")

    def create_pull_request(self):
            try:
                self.find_element("create_pull_request_button").click()
            except Exception as e:
                print(f"Error during creation: {str(e)}")
                raise

    def merge_pull_request(self):
        """Creates and merges a pull request after checking for conflicts."""
        try:
            time.sleep(10)
            self.driver.refresh()
            time.sleep(3)
            merge_button = self.find_element("merge_pr_button")
            assert self.find_element("no_conflict_text"), "Merge conflict detected! Cannot merge automatically."
            merge_button.click()
            time.sleep(3)
            confirm_button = self.find_element("confirm_merge_button")
            confirm_button.click()

        except Exception as e:
            raise RuntimeError(f"Error during merge: {str(e)}")

    def verify_merge_success(self):
        """Verifies if the PR merge was successful."""
        time.sleep(5)
        merge_success_text = self.find_element("merge_success_message").text
        if "Pull request successfully merged" in merge_success_text:
            print("Merge verification successful.")
            return True
        else:
            print("Merge verification failed.")
            return False

    def add_readme_in_empty_repo_and_change(self,branch_name):
        """Adds README file in an empty repository - main branch, change and commit in new branch"""
        self.find_element("add_readme_file").click()
        time.sleep(3)
        text_input = (self.find_element("file_content_input"))
        time.sleep(1)
        text_input.clear()
        time.sleep(1)
        text_input.send_keys("Testing - creating a README file")
        time.sleep(1)
        self.find_element("commit_changes_button").click()
        time.sleep(3)
        self.find_element("dialog_commit_button").click()
        time.sleep(3)
        self.find_element("edit_file_button").click()
        time.sleep(3)
        text_input = (self.find_element("file_content_input"))
        text_input.clear()
        text_input.send_keys("Testing - updated the README file")
        self.find_element("commit_changes_button").click()
        time.sleep(3)
        self.find_element("create_new_branch_checkbox").click()
        time.sleep(1)
        branch_input = self.find_element("branch_name_input")
        time.sleep(2)
        branch_input.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
        time.sleep(2)
        branch_input.send_keys(branch_name)
        time.sleep(2)
        self.find_element("propose_changes_button").click()

    def delete_branch_after_merge(self):
        self.find_element("delete_branch").click()
        time.sleep(1)