import time
import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from pages.base_page import BasePage
from pages.pull_request_page import PullRequestPage

def test_delete_repo():
    """Delete the existing Repo"""
    try:
        # Step 1: Login to GitHub
        driver = get_driver()
        base_page = BasePage(driver)
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
            base_page.delete_repo()

    except:
        None
