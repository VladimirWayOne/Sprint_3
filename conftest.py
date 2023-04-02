import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from mimesis import Person
from mimesis.enums import Locale
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import Locators
from tests.urls import Urls

locators = Locators()
urls = Urls


person = Person(locale=Locale.RU)


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1500,900")

    driver = webdriver.Chrome(options=options)
    driver.get(urls.url_main_paige)

    yield driver
    driver.quit()


@pytest.fixture()
def user_data():
    """
    Генерация валидных данных
    :return: dict()
    """
    full_name = person.full_name()
    password = person.password(length=6)
    email = person.email()
    user_data = {'full_name': full_name, 'password': password, 'email': email}
    # Запись данных в файл, чтобы не потерять
    user_creds = json.dumps(user_data)
    with open('json_data.json', 'w', encoding='utf-8') as outfile:
        outfile.write(user_creds)
    return user_data


@pytest.fixture()
def login(driver):
    """ Войти в аккаунт"""
    with open('json_data.json', 'r') as json_file:
        data = json.load(json_file)
    driver.get(urls.url_login)

    driver.find_element(*locators.locator_email_field).send_keys(
        data['email'])
    driver.find_element(*locators.locator_password_field).send_keys(data['password'])
    driver.find_element(*locators.locator_login_button_any_forms).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(locators.locator_order_button))
    return driver
