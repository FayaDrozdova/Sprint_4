from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка принятия куки
    ACCEPT_COOKIES_BUTTON = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]
    # Блок "Вопросы о важном"
    QUESTIONS_ABOUT_IMPORTANT_DIV = [By.XPATH, ".//div[text()='Вопросы о важном']"]
    # Блок со списком вопросов
    QUESTIONS_LIST_PARENT_DIV = [By.XPATH, ".//*[@class='accordion']"]
    # Список вопросов
    QUESTIONS_LIST_DIV = [By.XPATH, ".//*[contains(@id, 'accordion__heading-')]"]
    # Список ответов
    ANSWERS_LIST_DIV = [By.XPATH, ".//*[contains(@id, 'accordion__panel-')]/p"]
    # Кнопка заказа в шапке сайта
    ORDER_IN_HEADER_BUTTON = [By.XPATH, ".//*[@class='Button_Button__ra12g']"]
    # Кнопка заказа после блока шагов
    ORDER_AFTER_STEPS_BUTTON = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button"]
    # Логотип "Скутер"
    SCOOTER_LOGO = [By.XPATH, ".//*[@alt='Scooter']"]
    # Логотип "Яндекс"
    YANDEX_LOGO = [By.XPATH, ".//*[@alt='Yandex']"]
    # Поисковая строка на странице Яндекс Дзен
    SEARCH_ROW = [By.XPATH, ".//iframe[@class='dzen-search-arrow-common__frame' and @aria-label='Поиск Яндекса']"]