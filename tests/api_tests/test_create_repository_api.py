import pytest
from utils.api_utils.api_client import GitHubAPI

api = GitHubAPI()
OWNER = "yaswitabalu87"
REPO_NAME = "test-repo-api"

def test_create_repository():
    """Tests repository creation via API."""
    response = api.create_repository(REPO_NAME, private=False)
    assert response.status_code == 201, f"Failed to create repo: {response.json()}"
