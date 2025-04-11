from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome
from conftest import login

import curl
from locators import Locators


class TestPersonalCabinet:
    def test_click_personal_cabinet(self, driver_chrome, login):
        driver_chrome.get(curl.main_site)
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
        save_button = WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.SAVE_BUTTON))
        assert save_button.text == "Сохранить"
