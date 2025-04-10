import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import curl

@pytest.fixture()
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(curl.main_site)
    yield driver
    driver.quit()












#@pytest. fixture
#def login_in_account_chrome(driver_chrome):
    #driver_chrome.find_elesent(*Locators.BUT_PERSONAL_ACCOUNT).Click()
    #driver_chrome.find_elesent(*Locators.LOG_EMAIL).send_keys(data.LOGIN_EMAIL)
    #driver_chrome.find_elesent(*Locators.LOG_PASSADRD).send_keys(data.PASSW0RD)
    #driver_chrome.find_elesent(*Locators.BUT_LOGIN).click()
    #WebDriverWait(driver_chrome, 3).until(EC.element_to_be_clickable((By.XPATH,