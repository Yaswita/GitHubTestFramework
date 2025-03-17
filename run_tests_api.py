import os
import xml.etree.ElementTree as ET
import pytest
import datetime

# Base directory of the framework
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# XML file for API test order
API_XML_FILE = os.path.join(BASE_DIR,"GitHubTestFramework", "xml_files", "test_apis_order.xml")

# Report directory
REPORT_DIR = os.path.join(BASE_DIR,"GitHubTestFramework", "reports")
os.makedirs(REPORT_DIR, exist_ok=True)  # Ensure reports directory exists

# Read API test order
def get_api_test_order():
    if not os.path.exists(API_XML_FILE):
        raise FileNotFoundError(f"Test order file '{API_XML_FILE}' not found!")

    tree = ET.parse(API_XML_FILE)
    root = tree.getroot()
    return [test.text.strip() for test in root.findall("test")]

# Run API tests
def run_api_tests():
    test_cases = get_api_test_order()
    if not test_cases:
        print("Error: No test cases found in test_apis_order.xml")
        return

    print("Executing API tests:", test_cases)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    api_report = os.path.join(REPORT_DIR, f"api_test_report_{timestamp}.html")

    pytest_args = [
        *test_cases,
        f"--html={api_report}",
        "--self-contained-html",  # Ensures independent report (no external .css)
        "--alluredir=" + os.path.join(REPORT_DIR, "allure-results-api"),
    ]

    pytest.main(pytest_args)

if __name__ == "__main__":
    run_api_tests()
