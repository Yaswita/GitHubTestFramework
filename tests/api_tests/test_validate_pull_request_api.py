import pytest
from utils.api_utils.api_pr_validation import pr_validation

# Initialize once to fetch the latest PR number and branches

def test_get_pr_details():
    """Test PR details and metadata validation"""
    pr_val = pr_validation()
    pr_data = pr_val.get_pr_details()

    assert pr_data["base"]["ref"] == pr_val.base_branch, "Base branch mismatch!"
    assert pr_data["head"]["ref"] == pr_val.head_branch, "Head branch mismatch!"
    assert pr_data["state"] == "open", "PR is not open!"
    assert "title" in pr_data, "PR Title missing!"

def test_compare_branches():
    """Test PR branch comparison"""
    pr_val = pr_validation()
    comparison = pr_val.compare_branches()

    assert "total_commits" in comparison, "Total commits missing!"
    assert isinstance(comparison["commits"], list), "Commits data is not a list!"

def test_verify_pr_files():
    """Test files changed in PR"""
    pr_val = pr_validation()
    files = pr_val.verify_pr_files()

    assert isinstance(files, list), "Files data is not a list!"
    for file in files:
        assert "filename" in file, "Filename missing!"
        assert "status" in file, "File status missing!"
