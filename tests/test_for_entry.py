from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import curl
import data
from locators import Locators
from helper import generate_email

class TestLoginFunctionality:
    def test_login_via_main_button(self, driver_chrome):
        email = generate_email() # Генерируем новый email для теста
        driver_chrome.get(curl.main_site)  # Открываем главную страницу
        driver_chrome.find_element(*Locators.BUTTON_LOGIN_MAIN).click() # Находим и кликаем по кнопке "Войти в аккаунт"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))  # Ожидание, что кнопка "Войти" будет доступной для клика
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(email) # Вводим сгенерированный email в поле для авторизации
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD) # Вводим правильный пароль из файла data
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()  # Кликаем по кнопке "Войти"