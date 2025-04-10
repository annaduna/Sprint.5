from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome
from conftest import login

import curl
import data
from locators import Locators


class TestPersonalCabinet:
    def test_click_personal_cabinet(self, driver_chrome, login):
        driver_chrome.get(curl.main_site)  # Открываем главную страницу
        # driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()  # Находим и кликаем по кнопке "Личный кабинет"
        # WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))  # Ожидание, что кнопка "Войти" будет доступной для клика
        # driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)  # Вводим сгенерированный email в поле для авторизации
        # driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)  # Вводим правильный пароль из файла data
        # driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()  # Кликаем по кнопке "Войти"
        # WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
        save_button = WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.SAVE_BUTTON))
        assert save_button.text == "Сохранить"
