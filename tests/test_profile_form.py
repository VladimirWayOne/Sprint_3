from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome

class TestStellarBurgersProfileForm:
    def test_click_profile_button_open_profile_form(self, login):
        """ Открыть личный кабинет """
        driver: Chrome
        driver, user_data = login
        # Переход в личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        # Ждем пока исчезнет надпись 'Соберите бургер'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        assert 'https://stellarburgers.nomoreparties.site/account/profile' == driver.current_url

    def test_click_constructor_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор' """
        driver: Chrome
        driver, user_data = login
        # Переход в личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        # Ждем пока исчезнет надпись 'Соберите бургер'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login):
        """ Переход из личного кабинета в конструктор при нажатии на лого """
        driver: Chrome
        driver, user_data = login
        # Переход в личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        # Ждем пока исчезнет надпись 'Соберите бургер'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        driver.find_element(By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']").click()
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

