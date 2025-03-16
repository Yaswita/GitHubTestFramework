import requests
import configparser

# Load API config
config = configparser.ConfigParser()
config.read("config/api_config.ini")

BASE_URL = config["API"]["base_url"]
TOKEN = config["API"]["token"]
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

class GitHubAPI:
    @staticmethod
    def api_create_repository(repo_name, private=True):
        url = f"{BASE_URL}/user/repos"
        data = {"name": repo_name, "private": private}
        response = requests.post(url, json=data, headers=HEADERS)
        return response

    @staticmethod
    def api_get_repository(owner, repo_name):
        url = f"{BASE_URL}/repos/{owner}/{repo_name}"
        response = requests.get(url, headers=HEADERS)
        return response

    @staticmethod
    def api_create_issue(owner, repo_name, title, body=""):
        url = f"{BASE_URL}/repos/{owner}/{repo_name}/issues"
        data = {"title": title, "body": body}
        response = requests.post(url, json=data, headers=HEADERS)
        return response

    @staticmethod
    def api_create_pull_request(owner, repo_name, head, base, title):
        url = f"{BASE_URL}/repos/{owner}/{repo_name}/pulls"
        data = {"title": title, "head": head, "base": base}
        response = requests.post(url, json=data, headers=HEADERS)
        return response
