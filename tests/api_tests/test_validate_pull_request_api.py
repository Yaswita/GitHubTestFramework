import pytest
from utils.api_utils.api_pr_validation import pr_validation


def test_get_pr_details():
    """Test PR details and metadata validation"""
    pr_val = pr_validation()
    pr_data = pr_val.get_pr_details()

    assert pr_data["base"]["ref"] == "main", "Base branch mismatch!"

    # Use a dynamic comparison or pattern matching for the head branch
    head_branch = pr_data["head"]["ref"]
    assert head_branch.startswith("test-"), f"Unexpected head branch name: {head_branch}"

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
