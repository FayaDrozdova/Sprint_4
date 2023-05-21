import allure
import pytest
from data.user import user_1, user_2
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPageFillingData, RentPageFillingData


class TestOrder:

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize('enter_button, station, name, last_name, address_to_take, '
                             'phone_number, date, index, color_index, message',
                             [pytest.param(user_1.enter_button, user_1.station, user_1.name,
                                           user_1.last_name, user_1.address_to_take,
                                           user_1.phone_number, user_1.date, user_1.index,
                                           user_1.color_index, user_1.message),
                              pytest.param(user_2.enter_button, user_2.station, user_2.name,
                                           user_2.last_name, user_2.address_to_take,
                                           user_2.phone_number, user_2.date, user_2.index,
                                           user_2.color_index, user_2.message)])
    def test_order_success(self, driver, enter_button, station, name, last_name,
                   address_to_take, phone_number, date, index, color_index, message):
        main_page = MainPage(driver)
        order_page = OrderPageFillingData(driver)
        rent_page = RentPageFillingData(driver)
        main_page.accept_cookie()
        main_page.click_order(enter_button)

        order_page.filling_order_data(
            name=name,
            last_name=last_name,
            address_to_take=address_to_take,
            station=station,
            phone_number=phone_number)

        order_page.click_next()

        rent_page.filling_about_rent_date(
            date=date,
            index=index,
            color=color_index,
            message=message)

        rent_page.click_on_button_to_order()
        rent_page.click_yes_on_modal_menu()

        assert 'Заказ оформлен' in rent_page.completed_order(), \
            'Не отображается всплывающее окно с сообщением об успешном создании заказа'
