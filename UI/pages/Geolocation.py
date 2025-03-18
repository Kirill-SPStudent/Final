from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Geoloc ():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru")

    def change_city(self, term: str):
        """Ввод названия города"""
        self._driver.find_element(By.CSS_SELECTOR,
                                  '[class="header-city__title"]').click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  'class="button change-city__button change-city__button--cancel light-blue"').click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'class="city-modal__city-input"').send_keys(
                                     term, Keys.RETURN)
        self.driver.find_element(
            By.CSS_SELECTOR, 'class="cities-list__item"').click()

    def city(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'class="header-city__title"').text
