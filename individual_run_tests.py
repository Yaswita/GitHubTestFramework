import os
import pytest
import xml.etree.ElementTree as ET
import datetime

# Ensure reports directory exists
report_dir = "../reports"
if not os.path.exists(report_dir):
    os.makedirs(report_dir)


# Read test order from XML file
def get_test_order():
    xml_file = "xml_files/test_order.xml"
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"Test order file '{xml_file}' not found!")

    tree = ET.parse(xml_file)
    root = tree.getroot()

    test_files = [test.text.strip() for test in root.findall("test")]
    return test_files


def run_tests():
    test_cases = get_test_order()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for test in test_cases:
        test_name = os.path.basename(test).replace(".py", "")
        report_file = f"{report_dir}/{test_name}_{timestamp}.html"

        print(f"Running test: {test}")  # Debugging output

        pytest.main([
            test,
            f"--html={report_file}",
            "--self-contained-html",
            "--alluredir=reports/allure-results",
        ])


if __name__ == "__main__":
    run_tests()
