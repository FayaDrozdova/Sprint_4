import allure
from page_objects.main_page import MainPage


class TestLogo:
    @allure.title('Проверка перехода через логотип "Самоката"')
    def test_click_on_logo_scooter_success(self, driver):
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page = MainPage(driver)
        main_page.click_on_logo_scooter()
        main_page.check_tabs()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", \
            'Ожидается переход на главную страницу «Самоката».'

    @allure.title('Проверка перехода через логотип "Яндекс"')
    def test_click_on_logo_yandex_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_logo_yandex()
        main_page.check_tabs()
        assert driver.current_url == "https://dzen.ru/?yredirect=true", \
            'Ожидается открытие в новом окне главной страницы Яндекса (Дзен).'
