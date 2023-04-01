import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from mimesis import Person
from mimesis.enums import Locale
import json

person = Person(locale=Locale.RU)
url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1500,900")

    driver = webdriver.Chrome(options=options, executable_path=r"D:\Distrib\chromedriver.exe")
    driver.get(url)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
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
    outfile.close()
    return user_data
