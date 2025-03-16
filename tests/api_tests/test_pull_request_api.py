import pytest
from api_utils.github_api import GitHubAPI

def test_create_pull_request():
    owner = "your_github_username"
    repo_name = "test-repo-123"
    response = GitHubAPI.create_pull_request(owner, repo_name, "feature-branch", "main", "New PR")
    assert response.status_code == 201, f"Pull request creation failed: {response.json()}"
