from pages.base_page import BasePage
from locators import HomePageLocators, QuestionLocators
import allure

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(HomePageLocators.COOKIE_BUTTON)
        except:
            pass
    
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_top(self):
        self.click(HomePageLocators.ORDER_TOP_BUTTON)
    
    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_bottom(self):
        self.scroll_to_element(HomePageLocators.ORDER_BOTTOM_BUTTON)
        self.click(HomePageLocators.ORDER_BOTTOM_BUTTON)
    
    @allure.step("Кликнуть на вопрос")
    def click_question(self, index):
        self.scroll_to_element(QuestionLocators.get_question(index))
        self.click(QuestionLocators.get_question(index))
    
    @allure.step("Получить текст ответа")
    def get_answer_text(self, index):
        return self.get_text(QuestionLocators.get_answer(index))
    
    @allure.step("Нажать на логотип Самоката")
    def click_samokat_logo(self):
        self.click(HomePageLocators.SAMOKAT_LOGO)
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_js(HomePageLocators.YANDEX_LOGO)
