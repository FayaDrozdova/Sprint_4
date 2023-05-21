from dataclasses import dataclass
from page_objects.locators.main_page_locators import MainPageLocators


@dataclass
class User:
    enter_button: list
    station: str
    name: str
    last_name: str
    address_to_take: str
    phone_number: str
    date: str
    index: int
    color_index: int
    message: str


user_1 = User(MainPageLocators.ORDER_IN_HEADER_BUTTON,
                  "Черкизовская", "Иван", "Иванов",
                  "Москва, Амурская ул., д.2, стр.1, кв.5", "+79111111111",
                  "20.06.2023", 3, 1, "Удобно было бы с 17:00 до 20:00")


user_2 = User(MainPageLocators.ORDER_AFTER_STEPS_BUTTON,
                  "Речной вокзал", "Мирослав", "Немиров",
                  "Москва, Флотская ул., д.9, кв.20", "+79222222222",
                  "21.06.2023", 4, 0, "Позвоните заранее, за полчаса")
