from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

locators = Locators()


class TestStellarBurgersConstructorForm:
    def test_constructor_go_to_sauces_scroll_to_sauces(self, login):
        """Проверка перехода на соусы"""
        driver = login

        driver.find_element(*locators.locator_constructor_button).click()
        driver.find_element(*locators.locator_sauces_button).click()
        assert driver.find_element(*locators.locator_sauces_button).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect', "Не работает переход на выбор соусов"

    def test_constructor_go_to_bun_scroll_to_bun(self, login):
        """Проверка перехода на соусы"""
        driver = login

        driver.find_element(*locators.locator_constructor_button).click()
        driver.find_element(*locators.locator_sauces_button).click()
        driver.find_element(*locators.locator_sauces_ban).click()
        assert driver.find_element(*locators.locator_sauces_ban).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect', "Не работает переход на выбор булок"

    def test_constructor_go_to_filling_scroll_to_filling(self, login):
        """Проверка перехода на соусы"""
        driver = login

        driver.find_element(*locators.locator_constructor_button).click()
        driver.find_element(*locators.locator_sauces_filling).click()
        assert driver.find_element(*locators.locator_sauces_filling).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect', "Не работает переход на выбор Начинки"
