import allure
from selenium.webdriver import Keys
from page_objects.base_page import BasePage
from page_objects.locators.order_page_locators import OrderPageLocators


class OrderPageFillingData(BasePage):
    @allure.step('Ввод имени')
    def set_name(self, name):
        self.send_key(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Ввод фамилии')
    def set_last_name(self, last_name):
        self.send_key(OrderPageLocators.LAST_NAME_INPUT, last_name)

    @allure.step('Ввод адреса')
    def set_address(self, address):
        self.send_key(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Ввод номера телефона')
    def set_phone_number(self, phone_number):
        self.send_key(OrderPageLocators.PHONE_INPUT, phone_number)

    @allure.step('Выбор остановки метро')
    def set_metro_station(self, station):
        self.find_element(OrderPageLocators.SUBWAY_STATION_INPUT).click()
        self.send_key(OrderPageLocators.SUBWAY_STATION_INPUT, station)
        self.send_key(OrderPageLocators.SUBWAY_STATION_INPUT, Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step('Клик на кнопку продолжить')
    def click_next(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполнение формы "Для кого самокат"')
    def filling_order_data(self, name, last_name, address_to_take, station, phone_number):
        self.wait_element(OrderPageLocators.NAME_INPUT[1])
        self.wait_element(OrderPageLocators.LAST_NAME_INPUT[1])
        self.wait_element(OrderPageLocators.ADDRESS_INPUT[1])
        self.wait_element(OrderPageLocators.SUBWAY_STATION_INPUT[1])
        self.wait_element(OrderPageLocators.PHONE_INPUT[1])
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address_to_take)
        self.set_metro_station(station)
        self.set_phone_number(phone_number)


class RentPageFillingData(BasePage):
    @allure.step('Ввод даты доставки')
    def set_when_to_bring(self, date):
        self.send_key(OrderPageLocators.START_RENT_DATE_INPUT, date)

    @allure.step('Выбор срока аренды')
    def set_rental_period(self, index):
        self.find_element(OrderPageLocators.DURATION_RENT_INPUT).click()
        self.find_elements(OrderPageLocators.DURATION_RENT_DROPDOWN_LIST)[index].click()

    @allure.step('Выбор цвета самоката')
    def set_scooter_color(self, color_index):
        self.find_elements(OrderPageLocators.COLOR_SCOOTER_CHECKBOX)[color_index].click()

    @allure.step('Заполнение комментария для курьера')
    def set_comment_for_the_courier(self, message):
        self.send_key(OrderPageLocators.COMMENT_INPUT, message)

    @allure.step('Заполнение формы про аренду')
    def filling_about_rent_date(self, date, index, color, message):
        self.wait_element(OrderPageLocators.COMMENT_INPUT[1])
        self.set_when_to_bring(date)
        self.set_rental_period(index)
        self.set_scooter_color(color)
        self.set_comment_for_the_courier(message)

    @allure.step('Клик на  кнопку "Заказать"')
    def click_on_button_to_order(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Клик на кнопку "Да"')
    def click_yes_on_modal_menu(self):
        self.find_elements(OrderPageLocators.CREATE_ORDER_QUESTION_BUTTONS)[1].click()

    @allure.step('Получение информации об оформленном заказе')
    def completed_order(self):
        text = self.find_element(OrderPageLocators.INFO_ABOUT_ORDER_DIV).text
        return text
