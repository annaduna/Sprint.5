
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import curl
from locators import Locators

class TestTransitionToConstructor:
    def test_transition_from_the_private_to_a_constructor(self,driver_chrome,login):
        driver_chrome.find_element(*Locators.BUTTON_PERSONAL_CABINET).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.SAVE_BUTTON))
        driver_chrome.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.element_to_be_clickable(Locators.ORDER_BUTTON_LOCATOR))
        assert driver_chrome.current_url == curl.main_site
