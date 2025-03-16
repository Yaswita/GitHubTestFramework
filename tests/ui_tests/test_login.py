import time

import pytest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.webdriver_setup import get_driver

def test_login():
    driver = get_driver()
    login_page = LoginPage(driver)
    base_page = BasePage(driver)

    login_page.launch_application("https://github.com/login")
    login_page.login("GitHub")
    time.sleep((3))
    assert base_page.is_text_present("Home"), "Login successful, but 'Home' text not found."
    assert login_page.is_login_successful(), login_page.is_login_failed()

    driver.quit()
