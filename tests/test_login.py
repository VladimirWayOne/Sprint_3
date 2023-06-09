from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pytest

from locators import Locators
from urls import Urls

locators = Locators()
urls = Urls()


class TestStellarBurgersLoginForm:
    def test_login_sign_in_button_show_login_page(self, driver):
        """Проверка входа через кноку 'Войти в аккаунт'"""

        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        assert driver.current_url == urls.url_login

    def test_login_personal_account_button_show_login_page(self, driver):
        """Проверка входа через кноку 'Личный Кабинет'"""
        driver.find_element(*locators.locator_profile_button).click()
        assert driver.current_url == urls.url_login

    def test_login_registration_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме регистрации"""

        driver.get(urls.url_register)
        driver.find_element(*locators.locator_login_text_with_href).click()
        assert driver.current_url == urls.url_login

    def test_login_forgot_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля' этап ввода почты"""

        driver.get(urls.url_forgot_password)
        driver.find_element(*locators.locator_login_text_with_href).click()
        assert driver.current_url == urls.url_login

    def test_login_reset_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля' этап ввода нового пароля и кода из письма"""

        driver.get(urls.url_forgot_password)
        driver.find_element(*locators.locator_login_text_with_href).click()
        assert driver.current_url == urls.url_login

    def test_login_empty_email_and_password_nothing_happens(self, driver):
        """При нажатии на кнопку 'Войти' с пустым логином и паролем ничего не происходит: нет перехода к конструктору и не всплывает ошибка"""
        driver.get(urls.url_login)

        driver.find_element(*locators.locator_login_button_any_forms).click()
        order_buttons = driver.find_elements(*locators.locator_order_button)
        errors_messages = driver.find_elements(*locators.locator_error_message)
        assert len(order_buttons) == 0 and len(errors_messages) == 0

    def test_login_incorrect_email_nothing_happens(self, driver):
        """При вводе некорректного логина ничего не происходит: нет перехода к конструктору и не всплывает ошибка"""
        driver.get(urls.url_login)

        driver.find_element(*locators.locator_email_field).send_keys('qwe')

        driver.find_element(*locators.locator_login_button_any_forms).click()
        order_buttons = driver.find_elements(*locators.locator_order_button)
        errors_messages = driver.find_elements(*locators.locator_error_message)
        assert len(order_buttons) == 0 and len(errors_messages) == 0

    def test_login_incorrect_password_six_symbols_nothing_happens(self, driver):
        """При вводе некорректного пароля длинной 6 символов ничего не происходит: нет перехода к конструктору и не всплывает ошибка"""
        driver.get(urls.url_login)

        driver.find_element(*locators.locator_email_field).send_keys('qwe')
        driver.find_element(*locators.locator_password_field).send_keys("123456")

        driver.find_element(*locators.locator_login_button_any_forms).click()
        order_buttons = driver.find_elements(*locators.locator_order_button)
        errors_messages = driver.find_elements(*locators.locator_error_message)
        assert len(order_buttons) == 0 and len(errors_messages) == 0

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля длинной менее 6 символов отображает ошибку 'Некорректный пароль'"""
        driver.get(urls.url_login)

        driver.find_element(*locators.locator_email_field).send_keys('conclude2081@outlook.com')
        driver.find_element(*locators.locator_password_field).send_keys(password_list)
        driver.find_element(*locators.locator_login_button_any_forms).click()

        error_message = driver.find_element(*locators.locator_error_message)
        assert error_message.text == 'Некорректный пароль'

    def test_login_correct_email_and_password_show_main_page(self, login):
        """При вводе корректных данных отображается основная страничка"""
        driver = login
        assert driver.current_url == urls.url_main_paige
