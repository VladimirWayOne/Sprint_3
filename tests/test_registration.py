from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import *


class TestStellarBurgersRegistration:
    def test_registration_incorrect_email_show_error(self, driver):
        """
        При некорректном email появляется ошибка, что пользователь уже существует
        :param driver:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(*locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator_login_button))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_login_button).click()
        # Находим поле для ввода имени
        driver.find_element(*locator_name_field).send_keys(
            'Гавриил Анчаров')
        # Находим поле для ввода Email
        driver.find_element(*locator_email_field).send_keys('qwe')
        # Находим поле для ввода пароля
        driver.find_element(*locator_password_field).send_keys("""v)j"MY""")
        # Находим кнопку зарегистрироваться
        driver.find_element(*locator_register_button).click()
        # Ожидаем появления ошибки
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator_error_message))
        # Находим сообщение об ошибке
        error_message = driver.find_elements(*locator_error_message)
        # Видимо, отдельного текста ошибки некорретного email'a нет, поэтому просто проверяем наличие ошибки
        assert len(error_message) > 0

    def test_registration_empty_name_nothing_happens(self, driver):
        """
        При пустом поле Имя после нажатия на кнопку Зарегистрироваться ничего не происходит
        :param driver:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(*locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator_login_button))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_login_button).click()
        # Находим поле для ввода Email
        driver.find_element(*locator_email_field).send_keys('qwe@owfinwE.YU')
        # Находим поле для ввода пароля
        driver.find_element(*locator_password_field).send_keys("""v)j"MY""")
        old_DOM = driver.find_element(By.XPATH, ".//*")
        # Находим кнопку зарегистрироваться
        driver.find_element(*locator_register_button).click()
        # Немного времени, чтобы точно убедиться, что ничего не происходит
        time.sleep(2)
        new_DOM = driver.find_element(By.XPATH, ".//*")

        assert old_DOM == new_DOM

    def test_registration_incorrect_password_show_error(self, driver):
        """
        При некорректном пароле появляется ошибка 'Некорректный пароль'
        :param driver:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(*locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator_login_button))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_login_button).click()
        # Находим поле для ввода имени
        driver.find_element(*locator_email_field).send_keys(
            'Гавриил Анчаров')
        # Находим поле для ввода Email
        driver.find_element(*locator_email_field).send_keys('qwe')
        # Находим поле для ввода пароля
        driver.find_element(*locator_password_field).send_keys("123")
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_register_button).click()
        # Ожидаем появления ошибки
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(locator_error_message))
        # Находим сообщение об ошибке
        error_message = driver.find_element(*locator_error_message)
        assert error_message.text == 'Некорректный пароль'

    def test_registration_correct_email_and_pwd_successful_registration(self, driver, user_data):
        """
        При успешной регистрации перебрасывает на страницу входа
        :param driver:
        :param user_data:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(*locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator_login_button))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_login_button).click()
        # Находим поле для ввода имени
        driver.find_element(*locator_email_field).send_keys(
            user_data['full_name'])
        # Находим поле для ввода Email
        driver.find_element(*locator_email_field).send_keys(user_data['email'])
        # Находим поле для ввода пароля
        driver.find_element(*locator_password_field).send_keys(user_data['password'])
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(*locator_register_button).click()

        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(locator_element_with_login_text))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
