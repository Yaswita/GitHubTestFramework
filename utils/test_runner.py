import os
import pytest

# Ensure 'reports/' directory exists
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_tests():
    pytest.main([
        "--html=reports/latest_report.html",  # Generate pytest HTML report
        "--alluredir=reports/allure-results",  # Store Allure results
    ])

if __name__ == "__main__":
    run_tests()
