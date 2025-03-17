# GitHub Automation Framework

This framework provides automated testing for GitHub using both UI and API approaches.

## Pre-Conditions

1. Sign in to your GitHub user account
2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the credential setup:
   ```
   python utils/set_credential.py
   ```
   Enter your GitHub username and password when prompted (one-time entry, stored in credentials manager)
4. Set up your GitHub access token:
   ```
   python utils/api_utils/set_token.py
   ```
   Enter your GitHub personal access token when prompted (one-time entry, stored in credentials manager)

## Running Tests

### UI Tests
1. Execute UI test cases:
   ```
   python run_tests.py
   ```
2. Reports will be generated inside the `tests/reports` folder

### API Tests
1. Execute API test cases:
   ```
   python run_tests_api.py
   ```
2. Reports will be generated inside the `tests/reports` folder

### Individual Test Execution
To run specific tests:
```
python individual_run_tests.py
```

## Reset Environment
To delete repositories created during testing and reset for cleaner execution:
```
python test_delete_repo.py
```

## Test Reports

The test execution reports for UI can be found [here](reports/ui_test_report_2025-03-17_10-58-54.html)
The test execution reports for API can be found [here](reports/api_test_report_2025-03-17_12-21-32.html)

Download and open them in browser 