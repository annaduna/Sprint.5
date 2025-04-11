import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import curl
import data
from locators import Locators


@pytest.fixture()
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(curl.main_site)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver_chrome):
    driver_chrome.get(curl.main_site)
    driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
    WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))  # Ожидание, что кнопка "Войти" будет доступной для клика
    driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
    driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
    driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
    # return driver_chrome
    # WebDriverWait(driver_chrome, 3).until(expected_conditions.element_to_be_clickable((By.XPATH,