import requests
from utils.api_utils.set_token import retrieve_token

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"
OWNER = "yaswitabalu87"
REPO_NAME = "test-repo-api"
TOKEN = retrieve_token()
PR_NUMBER = 1  # Change this to the actual PR number
EXPECTED_HEAD_BRANCH = "feature-branch"
EXPECTED_BASE_BRANCH = "main"

# Headers for Authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}


class pr_validation:
    def get_pr_details(self):
        """Fetch PR details and validate metadata"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR details: {response.text}")

        pr_data = response.json()
        return pr_data

    def compare_branches(self):
        """Compare branches in PR"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/compare/{EXPECTED_BASE_BRANCH}...{EXPECTED_HEAD_BRANCH}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to compare branches: {response.text}")

        return response.json()

    def verify_pr_files(self):
        """Verify files changed in PR"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/files"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR files: {response.text}")

        return response.json()
