from selenium.webdriver.common.by import By


class Account():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru")

    def input_number_profile(self, term: int):
        """Ввод номера телефона, сразу после цифр +79"""
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="header-profile__button"]').click()
        self._driver.find_element(
            By.CSS_SELECTOR, '[id="tid-input"]').send_keys(term)

    def color_button_in_profile(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  '[class="app-button auth-modal__sms-button blue"]').value_of_css_property("background-color")
