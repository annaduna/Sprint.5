from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome
from conftest import login

import curl

from locators import Locators

# Выход по кнопке в личном кабинете
class TestLogout:
    def test_logaut(self, driver_chrome, login):
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.SAVE_BUTTON))
        driver_chrome.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        assert driver_chrome.current_url == curl.url_login
