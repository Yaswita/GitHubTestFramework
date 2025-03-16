from selenium import webdriver
import pytest

def get_driver(browser="chrome"):
    """ Returns a WebDriver instance for the given browser. """
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    """ Pytest fixture to initialize WebDriver based on browser type. """
    driver = get_driver(request.param)
    yield driver
    driver.quit()
