import pytest
from api_utils.github_api import GitHubAPI

def test_fetch_repository():
    owner = "your_github_username"
    repo_name = "test-repo-123"
    response = GitHubAPI.get_repository(owner, repo_name)
    assert response.status_code == 200, f"Repo fetch failed: {response.json()}"
