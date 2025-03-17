import pytest
from utils.api_utils.api_client import GitHubAPI

api = GitHubAPI()
OWNER = "yaswitabalu87"
REPO_NAME = "test-repo-api"

def test_get_repository():
    """Tests fetching repository details."""
    response = api.get_repository(OWNER, REPO_NAME)
    assert response.status_code == 200, f"Failed to fetch repo details: {response.json()}"
