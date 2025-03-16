import pytest
import requests
import configparser

config = configparser.ConfigParser()
config.read("config/api_config.ini")

BASE_URL = config["API"]["base_url"]
TOKEN = config["API"]["token"]
HEADERS = {"Authorization": f"token {TOKEN}"}

def test_invalid_token():
    invalid_headers = {"Authorization": "token invalid_token"}
    response = requests.get(f"{BASE_URL}/user/repos", headers=invalid_headers)
    assert response.status_code == 401, "Expected Unauthorized error for invalid token"
