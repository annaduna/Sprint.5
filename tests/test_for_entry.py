

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome
import curl
import data
from locators import Locators


class TestLoginFunctionality:
    def test_login_via_main_button(self, driver_chrome):
        driver_chrome.get(curl.main_site)  # Открываем главную страницу
        driver_chrome.find_element(*Locators.BUTTON_LOGIN_MAIN).click() # Находим и кликаем по кнопке "Войти в аккаунт"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))  # Ожидание, что кнопка "Войти" будет доступной для клика
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site


class TestLoginViaPersonalCabinet:  # Класс для тестирования входа через "Личный кабинет"
    def test_login(self, driver_chrome):
        driver_chrome.get(curl.main_site)  # Открываем главную страницу
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click() # Находим и кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN)) # Ожидание, что кнопка "Войти" будет доступной для клика
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL) # Вводим сгенерированный email в поле для авторизации
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD) # Вводим правильный пароль из файла data
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click() # Кликаем по кнопке "Войти"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site
#
#
class TestLoginViaRegistrationButton:  # Класс для тестирования входа через кнопку в форме регистрации
    def test_login(self, driver_chrome):
        driver_chrome.get(curl.url_registration)  # Открываем страницу регистрации
        button_login_from_registration = driver_chrome.find_element(*Locators.BUTTON_LOGIN_FROM_REGISTRATION) # Находим кнопку "Войти"
        driver_chrome.execute_script("arguments[0].scrollIntoView(true);", button_login_from_registration) # Прокручиваем страницу до кнопки "Войти"
        button_login_from_registration.click() # Нажимаем на кнопку "Войти"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.presence_of_element_located(Locators.BUTTON_LOGIN)) # Ожидание, что кнопка "Войти" на странице авторизации станет доступна для клика после этого действия
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL) # Вводим сгенерированный email в поле для авторизации
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD) # Вводим правильный пароль из файла data
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click() # Кликаем по кнопке "Войти"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site
#
# # Тестовый класс для восстановления пароля и входа
class TestLoginViaPasswordRecovery:
    def test_login_via_recovery_button(self, driver_chrome):
        driver_chrome.get(curl.url_login)  # Открываем страницу входа
        recovery_button = driver_chrome.find_element(*Locators.BUTTON_RECOVERY_PASSWORD)  # Находим кнопку "Восстановить пароль"
        driver_chrome.execute_script("arguments[0].scrollIntoView(true);", recovery_button) # прокручиваем до нее
        recovery_button.click()  # Нажимаем на кнопку восстановления пароля
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN_FROM_RECOVERY)).click()  # Нажимаем на кнопку "Войти" после восстановления пароля
          # Ждем перехода на новую страницу
        WebDriverWait(driver_chrome, 20).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN))  # Ожидаем, пока страница авторизации станет доступной
        driver_chrome.find_element(*Locators.FIELD_EMAIL_AUTHORIZATION).send_keys(data.LOGIN_EMAIL)  # Вводим email
        driver_chrome.find_element(*Locators.FIELD_PASSWORD_AUTHORIZATION).send_keys(data.PASSWORD)  # Вводим пароль
        driver_chrome.find_element(*Locators.BUTTON_LOGIN).click()  # Кликаем по кнопке "Войти"
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site

