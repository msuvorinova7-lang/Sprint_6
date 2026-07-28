from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Заполнить имя")
    def fill_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
    
    @allure.step("Заполнить фамилию")
    def fill_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
    
    @allure.step("Заполнить адрес")
    def fill_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
    
    @allure.step("Выбрать станцию метро")
    def select_metro(self, station_name):
        self.click(OrderPageLocators.METRO_INPUT)
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.wait_for_clickable(station_locator)
        self.click(station_locator)
    
    @allure.step("Заполнить телефон")
    def fill_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Нажать 'Далее'")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Заполнить дату доставки")
    def fill_delivery_date(self, date):
        self.click(OrderPageLocators.DATE_INPUT)
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        self.click(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Выбрать срок аренды")
    def select_rental_period(self, period_text):
        self.scroll_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.wait_for_clickable(OrderPageLocators.RENTAL_PERIOD)
        self.click(OrderPageLocators.RENTAL_PERIOD)
        period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period_text}']")
        self.wait_for_clickable(period_locator)
        self.click(period_locator)
    
    @allure.step("Выбрать чёрный цвет")
    def select_black_color(self):
        self.click(OrderPageLocators.COLOR_BLACK)
    
    @allure.step("Выбрать серый цвет")
    def select_grey_color(self):
        self.click(OrderPageLocators.COLOR_GREY)
    
    @allure.step("Заполнить комментарий")
    def fill_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step("Нажать 'Заказать'")
    def click_order(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_clickable(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_visibility(OrderPageLocators.CONFIRM_MODAL)
        self.wait_for_clickable(OrderPageLocators.CONFIRM_YES_BUTTON)
        self.scroll_to_element(OrderPageLocators.CONFIRM_YES_BUTTON)
        self.click_js(OrderPageLocators.CONFIRM_YES_BUTTON)
    
    @allure.step("Проверить, что заказ создан")
    def is_order_created(self):
        try:
            self.wait_for_visibility(OrderPageLocators.ORDER_SUCCESS_HEADER)
            return True
        except:
            return False
