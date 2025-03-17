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
        """Initialize PR validation by fetching the latest PR number and branches."""
        self.pr_number, self.head_branch, self.base_branch = self.get_latest_pr_info()
        if not self.pr_number:
            raise Exception("No open pull requests found.")

    def get_latest_pr_info(self):
        """Retrieve the latest open PR number and its branch details."""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls?state=open"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PRs: {response.text}")

        prs = response.json()
        if prs:
            latest_pr = prs[0]  # Get the most recent open PR
            pr_number = latest_pr["number"]
            head_branch = latest_pr["head"]["ref"]
            base_branch = latest_pr["base"]["ref"]
            return pr_number, head_branch, base_branch
        return None, None, None

    def get_pr_details(self):
        """Fetch PR details and validate metadata"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls/{self.pr_number}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR details: {response.text}")

        return response.json()

    def compare_branches(self):
        """Compare dynamically retrieved branches in PR"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/compare/{self.base_branch}...{self.head_branch}"
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
