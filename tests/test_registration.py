from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestStellarBurgersRegistration:
    def test_registration_incorrect_email_show_error(self, driver):
        """
        При некорректном email появляется ошибка, что пользователь уже существует
        :param driver:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        # Находим поле для ввода имени
        driver.find_element(By.XPATH,
                            ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']").send_keys(
            'Гавриил Анчаров')
        # Находим поле для ввода Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('qwe')
        # Находим поле для ввода пароля
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys("""v)j"MY""")
        # Находим кнопку зарегистрироваться
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        # Ожидаем появления ошибки
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, ".//p[contains(@class, 'input__error')]")))
        # Находим сообщение об ошибке
        error_message = driver.find_elements(By.XPATH, ".//p[contains(@class, 'input__error')]")
        # Видимо, отдельного текста ошибки некорретного email'a нет, поэтому просто проверяем наличие ошибки
        assert len(error_message) > 0

    def test_registration_empty_name_nothing_happens(self, driver):
        """
        При пустом поле Имя после нажатия на кнопку Зарегистрироваться ничего не происходит
        :param driver:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        # Находим поле для ввода Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('qwe@owfinwE.YU')
        # Находим поле для ввода пароля
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys("""v)j"MY""")
        old_DOM = driver.find_element(By.XPATH, ".//*")
        # Находим кнопку зарегистрироваться
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
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
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        # Находим поле для ввода имени
        driver.find_element(By.XPATH,
                            ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']").send_keys(
            'Гавриил Анчаров')
        # Находим поле для ввода Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys('qwe')
        # Находим поле для ввода пароля
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys("123")
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
        # Ожидаем появления ошибки
        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, ".//p[contains(@class, 'input__error')]")))
        # Находим сообщение об ошибке
        error_message = driver.find_element(By.XPATH, ".//p[contains(@class, 'input__error')]")
        assert error_message.text == 'Некорректный пароль'

    def test_registration_correct_email_and_pwd_successful_registration(self, driver, user_data):
        """
        При успешной регистрации перебрасывает на страницу входа
        :param driver:
        :param user_data:
        :return:
        """
        # Переходим в окно личного кабинета
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
        # Находим поле для ввода имени
        driver.find_element(By.XPATH,
                            ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']").send_keys(
            user_data['full_name'])
        # Находим поле для ввода Email
        driver.find_element(By.XPATH,
                            ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']").send_keys(user_data['email'])
        # Находим поле для ввода пароля
        driver.find_element(By.XPATH, ".//input[@type='password' and @name='Пароль']").send_keys(user_data['password'])
        # Находим кнопку зарегистрироваться и нажимаем
        driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH, ".//*[text() = 'Вход']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
