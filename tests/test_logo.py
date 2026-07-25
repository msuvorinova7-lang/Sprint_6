from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogo:
    def test_samokat_logo_redirects_to_home(self, driver):
        """Клик на логотип Самоката → главная страница"""
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        home_page.click_order_top()
        home_page.click_samokat_logo()
        
        current_url = driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/", \
            f"Неверный URL: {current_url}"
    
    def test_yandex_logo_opens_dzen(self, driver):
        """Клик на логотип Яндекса → открывается Дзен в новой вкладке"""
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        original_window = driver.current_window_handle
        
        # Клик на логотип Яндекса через JavaScript (более надёжно для Firefox)
        yandex_logo = driver.find_element(*home_page.YANDEX_LOGO)
        driver.execute_script("arguments[0].click();", yandex_logo)
        
        # Ждём появления новой вкладки
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        
        # Переключение на новую вкладку
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        # Ждём, пока URL загрузится (не about:blank)
        WebDriverWait(driver, 15).until(
            lambda d: d.current_url != "about:blank"
        )
        
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Неверный URL: {current_url}"
        
        # Закрыть вкладку и вернуться
        driver.close()
        driver.switch_to.window(original_window)
