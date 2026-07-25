import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

class TestQuestions:
    # Ожидаемые ответы (обновлённые)
    ANSWERS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]
    
    @pytest.mark.parametrize("question_index", range(8))
    def test_question_answer(self, driver, question_index):
        """Проверка ответов на вопросы"""
        home_page = HomePage(driver)
        home_page.accept_cookies()
        
        # Скролл до вопроса
        question = driver.find_element(By.ID, f"accordion__heading-{question_index}")
        driver.execute_script("arguments[0].scrollIntoView();", question)
        
        home_page.click_question(question_index)
        actual_answer = home_page.get_answer_text(question_index)
        expected_answer = self.ANSWERS[question_index]
        
        assert actual_answer == expected_answer, \
            f"Вопрос {question_index}. Ожидалось: {expected_answer}, Получено: {actual_answer}"
