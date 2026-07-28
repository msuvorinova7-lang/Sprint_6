from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

class OrderPageLocators:
    # Первая форма
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая форма
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    
    # Кнопка "Да"
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    
    # Цвета
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    
    # Сообщение об успехе
    ORDER_SUCCESS_HEADER = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Номер заказа:')]")

class QuestionLocators:
    @staticmethod
    def get_question(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def get_answer(index):
        return (By.ID, f"accordion__panel-{index}")
