import os
import xml.etree.ElementTree as ET
import pytest
import datetime

# Base directory of the framework
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# XML file for UI test order
UI_XML_FILE = os.path.join(BASE_DIR, "GitHubTestFramework","xml_files", "test_order.xml")
print(UI_XML_FILE)
# Report directory
REPORT_DIR = os.path.join(BASE_DIR,"GitHubTestFramework", "reports")
os.makedirs(REPORT_DIR, exist_ok=True)  # Ensure reports directory exists

# Read UI test order
def get_ui_test_order():
    if not os.path.exists(UI_XML_FILE):
        raise FileNotFoundError(f"Test order file '{UI_XML_FILE}' not found!")

    tree = ET.parse(UI_XML_FILE)
    root = tree.getroot()
    return [test.text.strip() for test in root.findall("test")]

# Run UI tests
def run_ui_tests():
    test_cases = get_ui_test_order()
    if not test_cases:
        print("Error: No test cases found in test_order.xml")
        return

    print("Executing UI tests:", test_cases)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ui_report = os.path.join(REPORT_DIR, f"ui_test_report_{timestamp}.html")

    pytest_args = [
        *test_cases,
        f"--html={ui_report}",
        "--self-contained-html",  # Ensures independent report (no external .css)
        "--alluredir=" + os.path.join(REPORT_DIR, "allure-results-ui"),
    ]

    pytest.main(pytest_args)

if __name__ == "__main__":
    run_ui_tests()
