from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import Locators
from urls import Urls

locators = Locators()
urls = Urls()

class TestStellarBurgersRegistration:
    def test_registration_incorrect_email_show_error(self, driver):
        """
        При некорректном email появляется ошибка, что пользователь уже существует
        :param driver:
        :return:
        """
        driver.find_element(*locators.locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locators.locator_login_button))

        driver.find_element(*locators.locator_login_button).click()

        driver.find_element(*locators.locator_name_field).send_keys(
            'Гавриил Анчаров')

        driver.find_element(*locators.locator_email_field).send_keys('qwe')

        driver.find_element(*locators.locator_password_field).send_keys("""v)j"MY""")

        driver.find_element(*locators.locator_register_button).click()

        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locators.locator_error_message))

        error_message = driver.find_elements(*locators.locator_error_message)

        assert len(error_message) > 0

    def test_registration_empty_name_nothing_happens(self, driver):
        """
        При пустом поле Имя после нажатия на кнопку Зарегистрироваться ничего не происходит: нет ошибки и нет перехода на страницу входа
        :param driver:
        :return:
        """

        driver.find_element(*locators.locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locators.locator_login_button))

        driver.find_element(*locators.locator_login_button).click()

        driver.find_element(*locators.locator_email_field).send_keys('qwe@owfinwE.YU')

        driver.find_element(*locators.locator_password_field).send_keys("""v)j"MY""")

        driver.find_element(*locators.locator_register_button).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(locators.locator_register_button))
        errors_messages = driver.find_elements(*locators.locator_error_message)
        assert driver.current_url == urls.url_register and len(errors_messages) == 0


    def test_registration_incorrect_password_show_error(self, driver):
        """
        При некорректном пароле появляется ошибка 'Некорректный пароль'
        :param driver:
        :return:
        """

        driver.find_element(*locators.locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locators.locator_login_button))

        driver.find_element(*locators.locator_login_button).click()

        driver.find_element(*locators.locator_email_field).send_keys(
            'Гавриил Анчаров')

        driver.find_element(*locators.locator_email_field).send_keys('qwe')

        driver.find_element(*locators.locator_password_field).send_keys("123")

        driver.find_element(*locators.locator_register_button).click()

        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(locators.locator_error_message))

        error_message = driver.find_element(*locators.locator_error_message)
        assert error_message.text == 'Некорректный пароль'

    def test_registration_correct_email_and_pwd_successful_registration(self, driver, user_data):
        """
        При успешной регистрации перебрасывает на страницу входа
        :param driver:
        :param user_data:
        :return:
        """

        driver.find_element(*locators.locator_profile_button).click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(locators.locator_login_button))

        driver.find_element(*locators.locator_login_button).click()

        driver.find_element(*locators.locator_name_field).send_keys(
            user_data['full_name'])

        driver.find_element(*locators.locator_email_field).send_keys(user_data['email'])

        driver.find_element(*locators.locator_password_field).send_keys(user_data['password'])

        driver.find_element(*locators.locator_register_button).click()

        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located(locators.locator_element_with_login_text))
        assert driver.current_url == urls.url_login
