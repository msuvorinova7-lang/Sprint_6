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
        
        original_window = home_page.get_current_window_handle()
        
        home_page.click_yandex_logo()
        
        # Ждём появления новой вкладки
        import time
        time.sleep(2)
        
        # Переключаемся на новую вкладку через BasePage
        home_page.switch_to_new_window(original_window)
        
        # Ждём загрузки страницы
        time.sleep(2)
        
        current_url = home_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Неверный URL: {current_url}"
        
        # Закрываем вкладку через BasePage
        home_page.close_current_window()
        home_page.switch_to_window(original_window)
