import pytest
from api_utils.github_api import GitHubAPI

def test_create_issue():
    owner = "your_github_username"
    repo_name = "test-repo-123"
    issue_title = "Bug in API Testing"
    response = GitHubAPI.create_issue(owner, repo_name, issue_title)
    assert response.status_code == 201, f"Issue creation failed: {response.json()}"
