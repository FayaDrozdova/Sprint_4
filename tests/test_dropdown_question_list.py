import pytest
import allure
from page_objects.main_page import MainPage
from page_objects.base_page import BasePage
from page_objects.locators.main_page_locators import MainPageLocators
from data.questions_about_important import QuestionsAboutImportant


class TestDropdownQuestionList:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    def test_click_on_question_answer_success(self, driver, question_index):
        main_page = MainPage(driver)
        base_page = BasePage(driver)
        main_page.accept_cookie()
        base_page.scroll_down()
        main_page.click_on_question_in_questions_about_important_block(question_index)
        actual_result = base_page.find_elements(MainPageLocators.ANSWERS_LIST_DIV)[question_index].text
        expected_result = QuestionsAboutImportant.QUESTION_AND_ANSWERS[
            base_page.find_elements(MainPageLocators.QUESTIONS_LIST_DIV)[question_index].text
        ]
        assert actual_result == expected_result, 'Ответ на вопрос не совпадает со значением в словаре'
