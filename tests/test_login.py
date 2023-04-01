from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pytest


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

    def test_login_empty_email_and_password_nothing_happens(self, driver):
        """При нажатии на кнопку 'Войти' с пустым логином и паролем ничего не происходит"""
        driver.get('https://stellarburgers.nomoreparties.site/login')
        # DOM до нажатия на кнопку 'Войти'
        old_DOM = driver.find_elements(By.XPATH, ".//*")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        # DOM после нажатия на кнопку 'Войти'
        new_DOM = driver.find_elements(By.XPATH, ".//*")
        assert old_DOM == new_DOM

    def test_login_incorrect_email_nothing_happens(self, driver):
        """При вводе некорректного логина ничего не происходит"""
        driver.get('https://stellarburgers.nomoreparties.site/login')
        # Локатор Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('qwe')
        # DOM до нажатия на кнопку 'Войти'
        old_DOM = driver.find_elements(By.XPATH, ".//*")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        # DOM после нажатия на кнопку 'Войти'
        new_DOM = driver.find_elements(By.XPATH, ".//*")
        assert old_DOM == new_DOM

    def test_login_incorrect_password_six_symbols_nothing_happens(self, driver):
        """При вводе некорректного пароля длинной 6 символов ничего не происходит"""
        driver.get('https://stellarburgers.nomoreparties.site/login')
        # Локатор Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('qwe')
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys("123456")
        # DOM до нажатия на кнопку 'Войти'
        old_DOM = driver.find_elements(By.XPATH, ".//*")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        # DOM после нажатия на кнопку 'Войти'
        new_DOM = driver.find_elements(By.XPATH, ".//*")
        assert old_DOM == new_DOM

    @pytest.mark.parametrize('password_list', ['1', '12345'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):
        """При вводе некорректного пароля длинной менее 6 символов отображает ошибку 'Некорректный пароль'"""
        driver.get('https://stellarburgers.nomoreparties.site/login')
        # Локатор Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('conclude2081@outlook.com')
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys(password_list)
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        # Находим сообщение об ошибке
        error_message = driver.find_element(By.XPATH, ".//p[contains(@class, 'input__error')]")
        assert error_message.text == 'Некорректный пароль'

    def test_login_correct_email_and_password_show_main_page(self, login):
        """При вводе корректных данных отображается основная страничка"""
        driver, _ = login
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

