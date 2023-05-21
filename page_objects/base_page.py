from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, xpath_element):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, f"{xpath_element}"))
        )

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator),
            f"Элемент с локатором {locator} не найден"
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(locator),
            f"Элементы с локатором {locator} не найдены"
           )

    def send_key(self, locator, name):
        self.find_element(locator).clear()
        return self.find_element(locator).send_keys(name)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollLow);")