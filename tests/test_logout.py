from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from locators import Locators
from urls import Urls

locators = Locators()
urls = Urls()

class TestStellarBurgersLogout:
    def test_click_profile_button_open_profile_form(self, login):
        """ Выйти из аккаунта """
        driver = login

        driver.find_element(*locators.locator_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.locator_info_message_profile))
        driver.find_element(*locators.locator_logout_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.locator_login_text_login_form))
        assert driver.current_url == urls.url_login
