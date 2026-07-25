from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class OrderPage:
    # Локаторы первой формы
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы второй формы
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
    
    # Сообщение об успешном заказе (без привязки к конкретному номеру)
    ORDER_SUCCESS_HEADER = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Номер заказа:')]")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def fill_name(self, name):
        element = self.wait.until(EC.visibility_of_element_located(self.NAME_INPUT))
        element.send_keys(name)
    
    def fill_surname(self, surname):
        element = self.wait.until(EC.visibility_of_element_located(self.SURNAME_INPUT))
        element.send_keys(surname)
    
    def fill_address(self, address):
        element = self.wait.until(EC.visibility_of_element_located(self.ADDRESS_INPUT))
        element.send_keys(address)
    
    def select_metro(self, station_name):
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT))
        metro_input.click()
        station = (By.XPATH, f"//div[text()='{station_name}']")
        self.wait.until(EC.element_to_be_clickable(station)).click()
    
    def fill_phone(self, phone):
        element = self.wait.until(EC.visibility_of_element_located(self.PHONE_INPUT))
        element.send_keys(phone)
    
    def click_next(self):
        element = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        element.click()
    
    def fill_delivery_date(self, date):
        date_input = self.wait.until(EC.element_to_be_clickable(self.DATE_INPUT))
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        self.driver.find_element(*self.ORDER_BUTTON).click()
    
    def select_rental_period(self, period_text):
        rental_field = self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", rental_field)
        time.sleep(0.5)
        rental_field.click()
        
        period = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period_text}']")
        self.wait.until(EC.element_to_be_clickable(period)).click()
    
    def select_color(self, color):
        if color.lower() in ["чёрный", "black"]:
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color.lower() in ["серая", "grey"]:
            self.driver.find_element(*self.COLOR_GREY).click()
    
    def fill_comment(self, comment):
        element = self.wait.until(EC.visibility_of_element_located(self.COMMENT_INPUT))
        element.send_keys(comment)
    
    def click_order(self):
        button = self.driver.find_element(*self.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(0.5)
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()
    
    def confirm_order(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MODAL))
            yes_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_YES_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", yes_button)
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].click();", yes_button)
        except TimeoutException:
            try:
                yes_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Да')]")))
                self.driver.execute_script("arguments[0].click();", yes_button)
            except:
                self.driver.execute_script("document.querySelector('button.Button_Button__ra12g').click();")
    
    def is_order_created(self):
        """Проверка, что заказ создан (номер заказа динамический)"""
        try:
            # Проверяем заголовок "Заказ оформлен"
            self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_HEADER))
            return True
        except TimeoutException:
            try:
                # Проверяем наличие текста "Номер заказа:" (номер может быть любым)
                element = self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_TEXT))
                # Дополнительная проверка: текст содержит номер (любая цифра)
                import re
                text = element.text
                return bool(re.search(r'Номер заказа:\s*\d+', text))
            except TimeoutException:
                return False
