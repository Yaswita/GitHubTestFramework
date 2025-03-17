import requests
from utils.api_utils.set_token import retrieve_token

# GitHub API URL
GITHUB_API_URL = "https://api.github.com"
OWNER = "yaswitabalu87"
REPO_NAME = "test-repo-api"
TOKEN = retrieve_token()

# Headers for Authentication
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}


class pr_validation:
    def __init__(self):
        # Dynamically fetch the PR number when the class is instantiated
        self.pr_number = self.get_latest_pr_number()

    def get_latest_pr_number(self):
        """Fetch the most recent open PR number"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls?state=open"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR list: {response.text}")

        pr_data = response.json()
        if not pr_data:
            raise Exception("No open PR found.")

        # Return the number of the most recent PR (first in the list)
        return pr_data[0]["number"]

    def get_pr_details(self):
        """Fetch PR details and validate metadata"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls/{self.pr_number}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR details: {response.text}")

        pr_data = response.json()
        return pr_data

    def compare_branches(self):
        """Compare branches in PR"""
        # Dynamically use the head and base branch names from PR details
        pr_data = self.get_pr_details()
        base_branch = pr_data["base"]["ref"]
        head_branch = pr_data["head"]["ref"]

        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/compare/{base_branch}...{head_branch}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise Exception(f"Failed to compare branches: {response.text}")

        return response.json()

    def verify_pr_files(self):
        """Verify files changed in PR"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls/{self.pr_number}/files"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR files: {response.text}")

        return response.json()
