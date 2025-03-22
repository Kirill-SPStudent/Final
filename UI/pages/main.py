from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MainPage ():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.chitai-gorod.ru")

    def searchfild(self, term: str):
        """Ввод названия товара"""
        self._driver.find_element(
            By.CSS_SELECTOR, '[class="header-search__input"]').send_keys(
                term, Keys.RETURN)

    def product_description(self):
        self._driver.find_elements(
            By.CSS_SELECTOR, '[class="product-card__caption"]')

    def add_to_card(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  '[class="chg-app-button chg-app-button--primary chg-app-button--s chg-app-button--brand-blue product-buttons__main-action product-buttons__main-action"]').click()

    def icon_on_card(self):
        self._driver.find_element(By.CSS_SELECTOR, '[class="chg-indicator chg-indicator--bg-cherry chg-indicator--mod-m-l header-controls__indicator header-controls__indicator"]').is_displayed()
