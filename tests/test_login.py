from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


class TestStellarBurgersLoginForm:
    """Проверка перехода в форму входа"""
    def test_login_sign_in_button_show_login_page(self, driver):
        """Проверка входа через кноку 'Войти в аккаунт'"""
        # Локатор кнопки 'Войти в аккаунт'
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_personal_account_button_show_login_page(self, driver):
        """Проверка входа через кноку 'Личный Кабинет'"""
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_registration_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме регистрации"""
        # Открываем форму регистрации
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_forgot_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля' этап ввода почты"""
        # Восстановление пароля
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_reset_password_form_sign_in_button(self, driver):
        """Проверка входа через кнопку 'Войти' в форме 'Восстановление пароля' этап ввода нового пароля и кода из письма"""
        # Восстановление пароля
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_login_incorrect_email_nothing_happens(self, driver):
        """При вводе некорректного логина ничего не происходит"""
        driver.get('https://stellarburgers.nomoreparties.site/login')
        old_DOM = driver.find_elements(By.XPATH, ".//*")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        new_DOM = driver.find_elements(By.XPATH, ".//*")
        assert old_DOM == new_DOM


