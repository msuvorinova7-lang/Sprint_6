from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    ORDER_TOP_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def accept_cookies(self):
        try:
            self.driver.find_element(*self.COOKIE_BUTTON).click()
        except:
            pass
    
    def click_order_top(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_TOP_BUTTON)).click()
    
    def click_order_bottom(self):
        button = self.driver.find_element(*self.ORDER_BOTTOM_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BOTTOM_BUTTON)).click()
    
    def click_question(self, index):
        question = (By.ID, f"accordion__heading-{index}")
        self.wait.until(EC.element_to_be_clickable(question)).click()
    
    def get_answer_text(self, index):
        answer = (By.ID, f"accordion__panel-{index}")
        self.wait.until(EC.visibility_of_element_located(answer))
        return self.driver.find_element(*answer).text
    
    def click_samokat_logo(self):
        self.driver.find_element(*self.SAMOKAT_LOGO).click()
    
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса через JavaScript (для Firefox)"""
        logo = self.driver.find_element(*self.YANDEX_LOGO)
        self.driver.execute_script("arguments[0].click();", logo)
