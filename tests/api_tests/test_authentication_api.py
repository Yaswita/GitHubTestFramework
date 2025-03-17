import pytest
import requests
from utils.api_utils.api_client import GitHubAPI
from utils.api_utils.set_token import retrieve_token

# Initialize API Client
api = GitHubAPI()
GITHUB_API_URL = "https://api.github.com"
OWNER = "yaswitabalu87"
PUBLIC_REPO_NAME = "test-repo-api"
PRIVATE_REPO_NAME = "private-repo-api"
TOKEN = retrieve_token()

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}


def test_valid_authentication():
    """Step 1: Test valid API authentication by accessing a public repository."""
    print("\n🔹 Running: test_valid_authentication")
    response = api.get_repository(OWNER, PUBLIC_REPO_NAME)
    assert response.status_code == 200, "Authentication failed for public repo"
    print("✅ Passed: Authentication for public repo")


def test_create_private_repository():
    """Step 2: Create a private repository for testing access control."""
    print("\n🔹 Running: test_create_private_repository")
    payload = {
        "name": PRIVATE_REPO_NAME,
        "description": "This is a private repo for testing",
        "private": True
    }
    response = requests.post(f"{GITHUB_API_URL}/user/repos", json=payload, headers=HEADERS)
    assert response.status_code == 201, "Failed to create private repository"
    print("✅ Passed: Private repository created")


def test_private_repository_access():
    """Step 3: Verify access to the private repository using valid authentication."""
    print("\n🔹 Running: test_private_repository_access")
    response = api.get_repository(OWNER, PRIVATE_REPO_NAME)
    assert response.status_code == 200, "Failed to access private repository with valid token"
    print("✅ Passed: Access to private repository verified")


def test_private_repository_invalid_token():
    """Step 4: Verify that an invalid token cannot access a private repository."""
    print("\n🔹 Running: test_private_repository_invalid_token")
    invalid_headers = {
        "Authorization": "Bearer invalid-token",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(f"{GITHUB_API_URL}/repos/{OWNER}/{PRIVATE_REPO_NAME}", headers=invalid_headers)
    print(response.json())
    assert response.status_code == 401, "Unauthorized access should fail (GitHub hides private repos)"
    print("✅ Passed: Private repo is inaccessible with invalid token")


def test_expired_token():
    """Step 5: Simulate an expired/revoked token scenario."""
    print("\n🔹 Running: test_expired_token")
    expired_token_headers = {
        "Authorization": "Bearer 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",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(f"{GITHUB_API_URL}/user", headers=expired_token_headers)
    assert response.status_code == 401, "Expired token should return unauthorized error"
    print("✅ Passed: Expired token handling verified")


def test_unauthorized_action():
    """Step 6: Attempt modifying a repository which is not yours - you don't have permission for"""
    repo_owner = "Yaswita"  # Change to an actual GitHub user
    repo_name = "finetune_jobs_api"  # Use a repo you don't have write access to
    payload = {"description": "Unauthorized update test"}

    response = requests.patch(f"{GITHUB_API_URL}/repos/{repo_owner}/{repo_name}", json=payload, headers=HEADERS)
    print(response.status_code, response.json())
    assert response.status_code in [404], "Unauthorized modification should fail"
    print("✅ Passed: Unauthorized action correctly rejected")


def test_delete_private_repository():
    """Step 7: Delete the private repository after validation."""
    print("\n🔹 Running: test_delete_private_repository")
    response = requests.delete(f"{GITHUB_API_URL}/repos/{OWNER}/{PRIVATE_REPO_NAME}", headers=HEADERS)
    assert response.status_code in [204, 404], "Private repo deletion failed or already deleted"
    print("✅ Passed: Private repository deleted")


def main():
    """Runs the tests in a predefined sequence to ensure correct execution."""
    print("\n🚀 Starting API Authentication & Permissions Testing...\n")

    try:
        test_valid_authentication()
        test_create_private_repository()
        test_private_repository_access()
        test_private_repository_invalid_token()
        test_expired_token()
        test_unauthorized_action()
        test_delete_private_repository()
    except AssertionError as e:
        print(f"❌ Test Failed: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")

    print("\n✅ All tests executed in sequence!")


if __name__ == "__main__":
    main()
