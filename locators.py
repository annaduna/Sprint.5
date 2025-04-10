from selenium.webdriver.common.by import By

class Locators:
            # Локаторы для регистрации
    REG_NAME = (By.XPATH, "//fieldset[1]//input[@name='name']")# поле ввода имени регистрации
    REG_EMAIL = (By.XPATH,"//fieldset[2]//input[@name='name']") # поле ввода email для регистрации
    REG_PASSWORD =(By.XPATH,"//input[@name='Пароль' and @type='password' and contains(@class, 'input__textfield')]") # поле ввода пароля для регистрации
    BUT_REG_END =(By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Зарегистрироваться')]") # кнопка завершения регистрации
    TEXT_INVALID_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']") # текст при невалидном вводе в поле пароль
            # Локаторы для проверки кнопки "Войти" с помощью:
    BUTTON_LOGIN_MAIN= (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]") #Локатор для кнопки "Войти в аккаунт" на главной странице
    FIELD_EMAIL_AUTHORIZATION = (By.XPATH, "//input[@name='name']")  # Локатор для поля ввода email (авторизация)
    FIELD_PASSWORD_AUTHORIZATION = (By.XPATH, "//input[@name='Пароль']") #Локатор для поля ввода пароля (авторизация)
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]") # Локатор для кнопки "Войти" на странице авторизации

    BUTTON_PERSONAL_CABINET = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]") # Локатор для кнопки "Личный кабинет"

    BUTTON_REGISTRATION = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]") # Локатор для кнопки "Зарегистрироваться" на странице авторизации

    BUTTON_LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Локатор для кнопки "Войти" на странице регистрации

    BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Локатор для кнопки "Восстановить пароль" на странице авторизации