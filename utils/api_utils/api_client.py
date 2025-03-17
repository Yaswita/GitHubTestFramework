import requests
from utils.api_utils.set_token import retrieve_token

class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.token = retrieve_token()
        self.headers = {"Authorization": f"Bearer {self.token}",
                        "Accept": "application/vnd.github.v3+json",
                        "Content-Type": "application/json"}

    def create_repository(self, repo_name, private=False):
        """Creates a GitHub repository."""
        url = f"{self.BASE_URL}/user/repos"
        payload = {"name": repo_name, "private": private}
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get_repository(self, owner, repo_name):
        """Fetches details of a GitHub repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers=self.headers)
        return response

    def create_issue(self, owner, repo, title, body=""):
        """Creates an issue in a repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        payload = {"title": title, "body": body}
        response = requests.post(url, json=payload, headers=self.headers)
        return response

    def get_issues(self, owner, repo):
        """Fetches details of a GitHub repository."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        response = requests.get(url, headers=self.headers)
        return response

    def create_pull_request(self, owner, repo, head, base, title, body=""):
        """Creates a pull request."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/pulls"
        payload = {"title": title, "head": head, "base": base, "body": body}
        response = requests.post(url, json=payload, headers=self.headers)
        return response
