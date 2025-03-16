import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage

def test_create_repository():
    driver = get_driver()
    login_page = LoginPage(driver)
    repo_page = RepositoryPage(driver)

    login_page.launch_application("https://github.com/login")
    login_page.login("GitHub")

    repo_name = "test-repo"  # Change this as needed
    expected_visibility = "public"  # Change to "private" if needed

    repo_page.create_repository(repo_name, is_private=False)

    # Verify repository details
    is_verified, message = repo_page.verify_repository_details(repo_name, expected_visibility)
    assert is_verified, message

    driver.quit()
