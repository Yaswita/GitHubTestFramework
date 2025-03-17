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

class pr_creation :
    def create_initial_commit(self):
        """Create an initial commit in the main branch"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/contents/README.md"
        payload = {
            "message": "Initial commit",
            "content": "SGVsbG8gd29ybGQh"  # Base64-encoded "Hello world!"
        }
        response = requests.put(url, headers=HEADERS, json=payload)
        if response.status_code not in [201, 200]:
            raise Exception(f"Failed to create initial commit: {response.text}")

        return response.json()

    def get_latest_commit_sha(self):
        """Fetch the latest commit SHA from the main branch"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/git/refs/heads/main"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to get commit SHA: {response.text}")

        return response.json()["object"]["sha"]

    def create_branch(self, branch_name, base_sha):
        """Create a new branch from a given base commit SHA"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/git/refs"
        payload = {"ref": f"refs/heads/{branch_name}", "sha": base_sha}
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code != 201:
            raise Exception(f"Failed to create branch: {response.text}")

        return response.json()

    def create_commit(self, branch_name):
        """Create a new commit in the given feature branch"""
        commit_message = "Adding a new feature"
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/git/commits"

        base_sha = self.get_latest_commit_sha()

        payload = {
            "message": commit_message,
            "tree": base_sha,
            "parents": [base_sha]
        }

        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code != 201:
            raise Exception(f"Failed to create commit: {response.text}")

        commit_sha = response.json()["sha"]
        self.update_branch(branch_name, commit_sha)
        return commit_sha

    def update_branch(self, branch_name, commit_sha):
        """Update the given branch with a new commit"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/git/refs/heads/{branch_name}"
        payload = {"sha": commit_sha, "force": True}
        response = requests.patch(url, headers=HEADERS, json=payload)
        if response.status_code != 200:
            raise Exception(f"Failed to update branch: {response.text}")

        return response.json()

    def create_pull_request(self, base_branch, head_branch):
        """Create a pull request (PR) from a feature branch to main"""
        url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO_NAME}/pulls"
        payload = {
            "title": "New Feature PR",
            "head": head_branch,
            "base": base_branch,
            "body": "Merging new feature branch into main"
        }
        response = requests.post(url, headers=HEADERS, json=payload)
        if response.status_code != 201:
            raise Exception(f"Failed to create pull request: {response.text}")

        return response.json()["html_url"]
