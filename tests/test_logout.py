from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from locators import *


class TestStellarBurgersLogout:
    def test_click_profile_button_open_profile_form(self, login):
        """ Выйти из аккаунта """
        driver: Chrome
        driver, _ = login
        # Переход в личный кабинет
        driver.find_element(*locator_profile_button).click()
        # Ждем пока появися надпись 'В этом разделе вы можете изменить свои персональные данные'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_info_message_profile))
        driver.find_element(*locator_logout_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_login_text_login_form))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'