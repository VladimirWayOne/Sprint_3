from selenium.webdriver.common.by import By


class Locators:
    
    locator_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")	                                                # Кнопка личного кабинета
    locator_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")                                                              # Кнопка "Зарегистрироваться" в форме /login
    locator_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")	            # Поле Имя при регистрации
    locator_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")	        # Поле Email при регистрации/входе
    locator_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")	                                # Поле Пароль при регистрации/входе
    locator_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")	                                        # Кнопка Зарегистрироваться в форме регистрации
    locator_error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]")	                                        # Сообщение об ошибке при регистрации
    locator_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")	                                                # Кнопка Оформить заказ
    locator_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")	                                            # Кнопка Войти в различных формах
    locator_info_message_profile = (By.XPATH, ".//p[contains(text(),'персональные данные']")                                # Надпись в личном кабинете
    locator_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")	                                                # Кнопка Конструктор
    locator_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")	                                            # Логотип вверху станицы
    locator_login_text_login_form = (By.XPATH, ".//h2[text()='Вход']")	                                                    # Надпись Вход в форме Логина
    locator_logout_button = (By.XPATH, ".//button[text()='Выход']")	                                                        # Кнопка Выход
    locator_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")                                                 # Кнопка Соусы
    locator_sauces_ban = (By.XPATH, ".//span[text()='Булки']/parent::*")                                                    # Кнопка Булки
    locator_sauces_filling = (By.XPATH, ".//span[text()='Начинки']/parent::*")                                              # Кнопка Начинки
    locator_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")                                                   # Элемент с надписью Вход
    locator_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")                                                       # Надпись Войти с ссылкой




