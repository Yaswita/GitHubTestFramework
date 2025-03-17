import pytest
from utils.api_utils.api_pr import pr_creation

TEST_BRANCH_NAME = "test-feature-branch"

def test_create_initial_commit():
    """Test initial commit creation"""
    pr = pr_creation()
    response = pr.create_initial_commit()
    assert "commit" in response, "Commit creation failed!"

def test_get_latest_commit_sha():
    """Test fetching latest commit SHA"""
    pr = pr_creation()
    sha = pr.get_latest_commit_sha()
    assert isinstance(sha, str) and len(sha) > 5, "Invalid commit SHA!"

def test_create_branch():
    """Test creating a new branch"""
    pr = pr_creation()
    base_sha = pr.get_latest_commit_sha()
    response = pr.create_branch(TEST_BRANCH_NAME, base_sha)
    assert response["ref"] == f"refs/heads/{TEST_BRANCH_NAME}", "Branch creation failed!"

def test_create_commit():
    """Test creating a commit in a branch"""
    pr = pr_creation()
    sha = pr.create_commit(TEST_BRANCH_NAME)
    assert isinstance(sha, str) and len(sha) > 5, "Invalid commit SHA!"

def test_create_pull_request():
    """Test creating a pull request"""
    pr = pr_creation()
    pr_url = pr.create_pull_request("main", TEST_BRANCH_NAME)
    assert pr_url.startswith("https://github.com"), "PR creation failed!"
