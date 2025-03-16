import time
import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from pages.base_page import BasePage
from pages.pull_request_page import PullRequestPage

def test_create_and_merge_pull_request():
    """Test case to check repository existence, create if missing, then create & merge a PR."""
    driver = get_driver()

    try:
        # Step 1: Login to GitHub
        driver = get_driver()
        login_page = LoginPage(driver)
        login_page.launch_application("https://github.com/login")
        login_result = login_page.login("GitHub")
        assert "Login successful!" in login_result, f"Login failed: {login_result}"

        # Step 2: Check if the repository exists
        repo_page = RepositoryPage(driver)
        repo_name = "test-repo"

        if repo_page.is_repository_present(repo_name):
            print(f"Repository '{repo_name}' already exists. Proceeding with tests.")
            time.sleep(2)
            repo_page.navigate_to_repository(repo_name)
            time.sleep(2)
        else:
            print(f"Repository '{repo_name}' not found. Creating a new repository.")
            repo_page.create_repository(repo_name, is_private=False)
            time.sleep(3)  # Wait for repo creation
            repo_page.navigate_to_repository(repo_name)

        pr_page = PullRequestPage(driver)

        branch_name = "feature-branch"
        # Step 3: Add a READ.ME file in an empty repository
        # change and commit in new branch
        time.sleep(5)
        pr_page.add_readme_in_empty_repo_and_change(branch_name)
        time.sleep(3)

        # Step 4: Create  and merge a pull request
        #pr_page.navigate_to("https://github.com/yaswitabalu87/test-repo/pull/1")
        pr_page.create_pull_request()
        time.sleep(3)
        pr_page.merge_pull_request()
        time.sleep(3)

        # Step 5: Verify merge success
        assert pr_page.verify_merge_success(), "Merge verification failed!"
        time.sleep(3)

        #Step 6: Delete branch after merge
        pr_page.delete_branch_after_merge()

    finally:
        driver.quit()
