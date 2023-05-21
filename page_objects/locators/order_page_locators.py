from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поле ввода "Имя"
    NAME_INPUT = [By.XPATH, ".//*[@placeholder='* Имя']"]
    # Поле ввода "Фамилия"
    LAST_NAME_INPUT = [By.XPATH, ".//*[@placeholder='* Фамилия']"]
    # Поле ввода "Адрес: куда привезти заказ"
    ADDRESS_INPUT = [By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"]
    # Поле ввода "Станция метро"
    SUBWAY_STATION_INPUT = [By.XPATH, ".//*[@placeholder='* Станция метро']"]
    # Поле ввода "Телефон: на него позвонит курьер"
    PHONE_INPUT = [By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"]
    # Кнопка "Далее"
    NEXT_BUTTON = [By.XPATH, ".//*[text()='Далее']"]
    # Поле "Когда привезти самокат"
    START_RENT_DATE_INPUT = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    # Поле "Срок аренды"
    DURATION_RENT_INPUT = [By.XPATH, ".//*[@class='Dropdown-arrow']"]
    # Выпадающий список "Срок аренды"
    DURATION_RENT_DROPDOWN_LIST = [By.XPATH, ".//*[@class='Dropdown-menu']/div"]
    # Цвет самоката
    COLOR_SCOOTER_CHECKBOX = [By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']"]
    # Поле "Комментарий для курьера
    COMMENT_INPUT = [By.XPATH, ".//*[@placeholder='Комментарий для курьера']"]
    # Кнопка "Заказать"
    ORDER_BUTTON = [By.XPATH,
                    ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"]
    # Кнопки ответов "Хотите оформить заказ?"
    CREATE_ORDER_QUESTION_BUTTONS = [By.XPATH,
                                     ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')" +
                                     "and text()='Нет' or text()='Да']"]
    # Блок информации о статусе заказа
    INFO_ABOUT_ORDER_DIV = [By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']"]
