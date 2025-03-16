import pytest
from utils.webdriver_setup import get_driver

@pytest.fixture(scope="session")
def driver():
    """ Initialize WebDriver once per test session. """
    driver = get_driver()
    yield driver  # Provide the WebDriver instance
    driver.quit()  # Close the browser after all tests are completed
