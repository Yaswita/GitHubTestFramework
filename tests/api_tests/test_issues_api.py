import pytest
from utils.api_utils.api_client import GitHubAPI

api = GitHubAPI()
OWNER = "yaswitabalu87"
REPO_NAME = "test-repo-api"

def test_create_and_get_issue():
    """Tests issue creation via API."""
    TITLE = "Bug in API"
    DESC = "Description of the bug"
    response = api.create_issue(OWNER, REPO_NAME, TITLE, DESC)
    assert response.status_code == 201, "Failed to create issue"

    """Tests issue retrival via API and check created issue is present"""
    response = api.get_issues(OWNER, REPO_NAME)
    issues = response.json()
    titles = [issue["title"] for issue in issues]  # Extract all issue titles
    assert TITLE in titles, f"Issue with title '{TITLE}' not found in response."
