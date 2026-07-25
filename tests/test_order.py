import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage

class TestOrder:
    @pytest.mark.parametrize("order_data", [
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина, 1",
            "metro": "Сокольники",
            "phone": "+79998887766",
            "date": "25.07.2026",
            "period": "сутки",
            "color": "чёрный",
            "comment": "Позвоните за час"
        },
        {
            "name": "Мария",
            "surname": "Иванова",
            "address": "пр. Мира, 5",
            "metro": "Театральная",
            "phone": "+79112223344",
            "date": "26.07.2026",
            "period": "двое суток",
            "color": "серая",
            "comment": "Без звонка"
        }
    ])
    @pytest.mark.parametrize("button_position", ["top", "bottom"])
    def test_positive_order(self, driver, order_data, button_position):
        """Позитивный сценарий заказа"""
        home_page = HomePage(driver)
        home_page.accept_cookies()

        if button_position == "top":
            home_page.click_order_top()
        else:
            home_page.click_order_bottom()

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
        order_page.select_color(order_data["color"])
        order_page.fill_comment(order_data["comment"])
        order_page.click_order()

        # Подтверждение
        order_page.confirm_order()

        assert order_page.is_order_created(), "Заказ не создан"
