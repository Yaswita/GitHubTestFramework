import pytest
from utils.api_utils.api_pr_validation import pr_validation

EXPECTED_HEAD_BRANCH = "feature-branch"
EXPECTED_BASE_BRANCH = "main"


def test_get_pr_details():
    """Test PR details and metadata validation"""
    pr_data = pr_validation.get_pr_details()

    assert pr_data["base"]["ref"] == EXPECTED_BASE_BRANCH, "Base branch mismatch!"
    assert pr_data["head"]["ref"] == EXPECTED_HEAD_BRANCH, "Head branch mismatch!"
    assert pr_data["state"] == "open", "PR is not open!"
    assert "title" in pr_data, "PR Title missing!"


def test_compare_branches():
    """Test PR branch comparison"""
    comparison = pr_validation.compare_branches()

    assert "total_commits" in comparison, "Total commits missing!"
    assert isinstance(comparison["commits"], list), "Commits data is not a list!"


def test_verify_pr_files():
    """Test files changed in PR"""
    files = pr_validation.verify_pr_files()

    assert isinstance(files, list), "Files data is not a list!"
    for file in files:
        assert "filename" in file, "Filename missing!"
        assert "status" in file, "File status missing!"
