import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from pages.issue_page import IssuesPage
import time


def test_create_issue():
    driver = get_driver()
    login_page = LoginPage(driver)
    repo_page = RepositoryPage(driver)
    issue_page = IssuesPage(driver)
    # Login to GitHub
    login_page.launch_application("https://github.com/login")
    login_page.login("GitHub")

    repo_name = "test-repo"

    # Check if repo exists
    if repo_page.is_repository_present(repo_name):
        print(f"Repository '{repo_name}' already exists. Navigating to it.")
        repo_page.navigate_to_repository(repo_name)
        time.sleep(3)
    else:
        print(f"Repository '{repo_name}' not found. Creating a new one.")
        repo_page.create_repository(repo_name, private=False)
        time.sleep(3)

    # Navigate to issues section
    repo_page.navigate_to_issues()
    time.sleep(2)
    # Create a new issue
    issue_title = "Test Issue for Bug Fix"
    label = "bug"
    assignee = "your-github-username"  # Replace with actual username

    issue_page.create_issue(issue_title, label=label, assignee=assignee)

    # Step 2: Verify Issue is Listed
    time.sleep(2)
    assert issue_page.verify_issue_exists(issue_title), "Issue not found in listing!"

    # Step 3: Verify Notification Received
    # assert issue_page.verify_notification_received(), "No notification received for issue creation."

    driver.quit()
