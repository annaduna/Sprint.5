from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import curl
import data
from locators import Locators
from helper import generate_email

class TestRegistrationChrome:
    def test_success_registration_chrome(self, driver_chrome):
        email = generate_email()
        driver_chrome.get(curl.url_registration)
        driver_chrome.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_chrome.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_chrome.find_element(*Locators.REG_PASSWORD).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUT_REG_END).click()
        WebDriverWait(driver_chrome, 3).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        assert driver_chrome.current_url == curl.url_login


class TestRegistrationWIthInvalidPasswordChrome:
    def test_invalid_registration_chrome(self, driver_chrome):
        email = generate_email()
        driver_chrome.get(curl.url_registration)
        driver_chrome.find_element(*Locators.REG_NAME).send_keys(data.NAME)
        driver_chrome.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver_chrome.find_element(*Locators.REG_PASSWORD).send_keys(data.INVALID_PASSWORD)
        driver_chrome.find_element(*Locators.BUT_REG_END).click()
        invalid_password_text_element = WebDriverWait(driver_chrome, 3).until(expected_conditions.visibility_of_element_located(Locators.TEXT_INVALID_PASSWORD))
        assert invalid_password_text_element.text == 'Некорректный пароль'





