from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver_chrome


from locators import Locators


class TestSections:
# class TestBunsSection:
    def test_click_buns_section(self,driver_chrome):
        driver_chrome.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.SAUCES_TAB,"class", "tab_tab_type_current__2BEPc"))
        driver_chrome.find_element(*Locators.BUNS_TAB).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BUNS_TAB, "class","tab_tab_type_current__2BEPc"))
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.BUNS_TAB).get_attribute("class")

# class TestSaucesSection:
    def test_click_sauces_section(self,driver_chrome):
        driver_chrome.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.SAUCES_TAB, "class", "tab_tab_type_current__2BEPc"))
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.SAUCES_TAB).get_attribute("class")

# class TestFillingsSection:
    def test_click_fillings_section(self,driver_chrome):
        driver_chrome.find_element(*Locators.FILLINGS_TAB).click()
        WebDriverWait(driver_chrome, 10).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.FILLINGS_TAB, "class", "tab_tab_type_current__2BEPc"))
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*Locators.FILLINGS_TAB).get_attribute("class")

