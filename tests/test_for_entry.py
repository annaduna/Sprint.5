from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome
import curl
import data
from locators import Locators


class TestLoginFunctionality:
    def test_login_via_main_button(self, driver_chrome):
        driver_chrome.get(curl.main_site)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site

    def test_login(self, driver_chrome):
        driver_chrome.get(curl.main_site)
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site

    def test_login(self, driver_chrome):
        driver_chrome.get(curl.url_registration)
        button_login_from_registration = driver_chrome.find_element(*Locators.BUTTON_LOGIN_FROM_REGISTRATION)
        driver_chrome.execute_script("arguments[0].scrollIntoView(true);", button_login_from_registration)
        button_login_from_registration.click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.presence_of_element_located(Locators.BUTTON_LOGIN))
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site

    def test_login_via_recovery_button(self, driver_chrome):
        driver_chrome.get(curl.url_login)
        recovery_button = driver_chrome.find_element(*Locators.BUTTON_RECOVERY_PASSWORD)
        driver_chrome.execute_script("arguments[0].scrollIntoView(true);", recovery_button)
        recovery_button.click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN_FROM_RECOVERY)).click()
        WebDriverWait(driver_chrome, 20).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site

