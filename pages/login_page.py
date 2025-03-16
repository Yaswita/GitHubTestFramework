from pages.base_page import BasePage
from utils.credential_manager import get_credentials
from utils.logger import get_logger
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger()

    def login(self, service):
        """Logs into GitHub using stored credentials."""
        try:
            # Retrieve stored credentials
            username, password = get_credentials(service)

            # Locate input fields and submit button
            username_field = self.find_element("username_input")
            password_field = self.find_element("password_input")
            submit_button = self.find_element("signin_button")

            # Enter credentials
            username_field.send_keys(username)
            password_field.send_keys(password)
            submit_button.click()

            # Verify login success
            if self.is_login_successful():
                self.logger.info("Login successful!")
                return "Login successful!"

            # If login failed, fetch and log error message
            login_error = self.get_login_error()
            self.logger.error(f"Login failed: {login_error}")
            return f"Login failed: {login_error}"

        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {str(e)}")
            return f"Error: Element not found - {str(e)}"

    def is_login_successful(self):
        """Check if login is successful by verifying page title."""
        return "GitHub" in self.driver.title

    def get_login_error(self):
        """Fetches login error messages from the page (invalid credentials, empty fields)."""
        try:
            error_element = self.find_element("login_error_message")
            return error_element.text if error_element else "Unknown login error"
        except NoSuchElementException:
            return "Unknown login error"
