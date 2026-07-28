import allure
import pytest
from pages.home_page import HomePage

@allure.epic("Тесты логотипов")
class TestLogo:
    
    @allure.title("Клик на логотип Самоката → переход на главную страницу")
    @allure.feature("Логотип Самоката")
    @allure.story("Переход на главную")
    def test_samokat_logo_redirects_to_home(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        home_page.click_order_top()
        home_page.click_samokat_logo()
        
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        current_url = home_page.get_current_url()
        assert current_url == expected_url, f"Неверный URL: {current_url}"
    
    @allure.title("Клик на логотип Яндекса → открывается Дзен в новой вкладке")
    @allure.feature("Логотип Яндекса")
    @allure.story("Открытие в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        window_count_before = len(home_page.get_window_handles())
        
        home_page.click_yandex_logo()
        
        home_page.wait_for_new_window(window_count_before)
        home_page.switch_to_new_window()
        home_page.wait_for_url_change("about:blank")
        
        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Неверный URL: {current_url}"
        
        home_page.close_current_window()
        home_page.switch_to_window_by_index(0)
