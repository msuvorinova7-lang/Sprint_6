import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.epic("Тесты заказа")
class TestOrder:
    
    # Данные для заказа через верхнюю кнопку
    order_data_top = [
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина, 1",
            "metro": "Сокольники",
            "phone": "+79998887766",
            "date": "25.07.2026",
            "period": "сутки",
            "comment": "Позвоните за час",
            "color_method": "select_black_color"
        },
        {
            "name": "Мария",
            "surname": "Иванова",
            "address": "пр. Мира, 5",
            "metro": "Театральная",
            "phone": "+79112223344",
            "date": "26.07.2026",
            "period": "двое суток",
            "comment": "Без звонка",
            "color_method": "select_grey_color"
        }
    ]
    
    # Данные для заказа через нижнюю кнопку
    order_data_bottom = [
        {
            "name": "Петр",
            "surname": "Сидоров",
            "address": "ул. Пушкина, 10",
            "metro": "Парк культуры",
            "phone": "+79998887755",
            "date": "27.07.2026",
            "period": "трое суток",
            "comment": "Домофон не работает",
            "color_method": "select_black_color"
        },
        {
            "name": "Елена",
            "surname": "Козлова",
            "address": "пр. Вернадского, 15",
            "metro": "Университет",
            "phone": "+79112223355",
            "date": "28.07.2026",
            "period": "сутки",
            "comment": "Позвонить за 30 минут",
            "color_method": "select_grey_color"
        }
    ]
    
    @allure.title("Позитивный сценарий заказа через верхнюю кнопку, данные: {order_data[name]}")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", order_data_top)
    def test_positive_order_top_button(self, driver, order_data):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        home_page.click_order_top()
        
        self._fill_order_form(driver, order_data)
    
    @allure.title("Позитивный сценарий заказа через нижнюю кнопку, данные: {order_data[name]}")
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", order_data_bottom)
    def test_positive_order_bottom_button(self, driver, order_data):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        home_page.click_order_bottom()
        
        self._fill_order_form(driver, order_data)
    
    def _fill_order_form(self, driver, order_data):
        """Вспомогательный метод для заполнения формы заказа"""
        order_page = OrderPage(driver)
        
        # Первая форма
        order_page.fill_name(order_data["name"])
        order_page.fill_surname(order_data["surname"])
        order_page.fill_address(order_data["address"])
        order_page.select_metro(order_data["metro"])
        order_page.fill_phone(order_data["phone"])
        order_page.click_next()
        
        # Вторая форма
        order_page.fill_delivery_date(order_data["date"])
        order_page.select_rental_period(order_data["period"])
        
        # Выбор цвета через динамический вызов метода (без условий)
        color_method = getattr(order_page, order_data["color_method"])
        color_method()
        
        order_page.fill_comment(order_data["comment"])
        order_page.click_order()
        
        order_page.confirm_order()
        
        assert order_page.is_order_created(), "Заказ не создан"
