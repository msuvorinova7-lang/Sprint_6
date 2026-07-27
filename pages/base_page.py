from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Найти все элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step("Ввести текст")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    @allure.step("Прокрутить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Клик через JavaScript")
    def click_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Ожидать видимость элемента")
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидать кликабельность элемента")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self, original_window):
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
    
    @allure.step("Закрыть текущую вкладку")
    def close_current_window(self):
        self.driver.close()
    
    @allure.step("Переключиться на вкладку")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    @allure.step("Получить все окна")
    def get_window_handles(self):
        return self.driver.window_handles
    
    @allure.step("Получить текущее окно")
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Ожидать появления новой вкладки")
    def wait_for_new_window(self, original_window):
        self.wait.until(lambda d: len(d.window_handles) > 1)
    
    @allure.step("Ожидать изменения URL")
    def wait_for_url_change(self, url):
        self.wait.until(lambda d: d.current_url != url)
    
    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.driver.execute_script("document.querySelector('button.Button_Button__ra12g').click();")
