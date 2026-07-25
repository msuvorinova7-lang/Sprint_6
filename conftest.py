import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    """Фикстура для Firefox"""
    # Опции Firefox
    options = Options()
    # Раскомментируй, если Firefox в нестандартной папке:
    # options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    
    # Автоматическая загрузка GeckoDriver
    service = Service(GeckoDriverManager().install())
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()
