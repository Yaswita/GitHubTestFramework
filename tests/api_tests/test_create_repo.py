import pytest
from api_utils.github_api import GitHubAPI

def test_create_repository():
    repo_name = "test-repo-123"
    response = GitHubAPI.create_repository(repo_name)
    assert response.status_code == 201, f"Failed to create repo: {response.json()}"
    assert response.json()["name"] == repo_name
