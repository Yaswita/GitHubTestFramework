from pages.navigation_page import NavigationPage
import time
import pytest
from utils.webdriver_setup import get_driver
from pages.login_page import LoginPage
from pages.repository_page import RepositoryPage
from pages.base_page import BasePage
from pages.pull_request_page import PullRequestPage

@pytest.mark.navigation
def test_navigate_tabs(driver):
    """Test seamless navigation between repository tabs."""
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

    # Step 3: Navigate between tabs and check if they are active
    navigation = NavigationPage(driver)
    tabs = ["code", "issues", "pull_requests"]  # Defined in object.ini

    for tab in tabs:
        navigation.click_tab(tab)
        assert navigation.is_tab_active(tab), f"{tab} is not active!"

    # Step 4: Check pagination is present or not
    pagination_present = navigation.check_pagination_exists()
    if pagination_present:
        print("Pagination is present.")
    else:
        print("Pagination is NOT present, but this does not cause failure.")

