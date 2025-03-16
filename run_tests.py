import os
import pytest
import xml.etree.ElementTree as ET
import datetime

# Ensure reports directory exists
report_dir = "reports"
if not os.path.exists(report_dir):
    os.makedirs(report_dir)


# Read test order from XML file
def get_test_order():
    xml_file = "test_order.xml"
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"Test order file '{xml_file}' not found!")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    test_files = [test.text.strip() for test in root.findall("test")]
    return test_files


def run_tests():
    test_cases = get_test_order()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    combined_report = f"{report_dir}/combined_report_{timestamp}.html"

    pytest_args = [
        *test_cases,  # Run tests in sequence
        f"--html={combined_report}",
        "--self-contained-html",
        "--alluredir=reports/allure-results",
    ]

    pytest.main(pytest_args)


if __name__ == "__main__":
    run_tests()
