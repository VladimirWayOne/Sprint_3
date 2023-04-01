from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


class TestStellarBurgersLogout:
    def test_click_profile_button_open_profile_form(self, login):
        """ Выйти из аккаунта """
        driver: Chrome
        driver, user_data = login
        # Переход в личный кабинет
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        # Ждем пока появися надпись 'В этом разделе вы можете изменить свои персональные данные'
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Вход']")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'