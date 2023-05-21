from page_objects.base_page import BasePage
import allure
from page_objects.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        cookie = self.find_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)
        cookie.click()

    @allure.step('Кликаем на вопрос выпадающего списка в разделе "Вопросы о важном"')
    def click_on_question_in_questions_about_important_block(self, question_index):
        self.wait_element(MainPageLocators.QUESTIONS_ABOUT_IMPORTANT_DIV[1])
        self.wait_element(MainPageLocators.QUESTIONS_LIST_PARENT_DIV[1])
        button_accordions = self.find_elements(MainPageLocators.QUESTIONS_LIST_DIV)
        button_accordions[question_index].click()
        self.wait_element(MainPageLocators.QUESTIONS_LIST_PARENT_DIV[1])
        self.wait_element(MainPageLocators.QUESTIONS_LIST_DIV[1])
        self.wait_element(MainPageLocators.QUESTIONS_LIST_PARENT_DIV[1])

    @allure.step('Кликаем на кнопку логотипа Самоката')
    def click_on_logo_scooter(self):
        click_on_logo = self.find_element(MainPageLocators.SCOOTER_LOGO)
        click_on_logo.click()

    @allure.step('Кликаем на кнопку логотипа Яндекса')
    def click_on_logo_yandex(self):
        self.find_element(MainPageLocators.YANDEX_LOGO).click()

    @allure.step('Проверяем вкладки')
    def check_tabs(self):
        number_of_tabs = len(self.driver.window_handles)
        if number_of_tabs > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.wait_element(MainPageLocators.SEARCH_ROW[1])

    @allure.step('Кликаем кнопку на кнопку "Заказать"')
    def click_order(self, xpath_element):
        self.find_element(xpath_element).click()