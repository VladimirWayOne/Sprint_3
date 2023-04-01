from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from locators import *
class TestStellarBurgersProfileForm:
    def test_click_profile_button_open_profile_form(self, login):
        """ Открыть личный кабинет """
        driver: Chrome
        driver, _ = login
        # Переход в личный кабинет
        driver.find_element(*locator_profile_button).click()
        # Ждем пока исчезнет надпись 'Соберите бургер'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_info_message_profile))
        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url

    def test_click_constructor_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор' """
        driver: Chrome
        driver, _ = login
        # Переход в личный кабинет
        driver.find_element(*locator_profile_button).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_info_message_profile))
        driver.find_element(*locator_constructor_button).click()
        #  Надпись 'Соберите бургер'
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии на лого """
        driver: Chrome
        driver, _ = login
        # Переход в личный кабинет
        driver.find_element(*locator_profile_button).click()
        # Ждем пока исчезнет надпись 'Соберите бургер'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_info_message_profile))
        driver.find_element(*locator_logo).click()
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

