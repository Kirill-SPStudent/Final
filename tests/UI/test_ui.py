import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://www.chitai-gorod.ru/")


def test_search():
    driver.find_element(By.CSS_SELECTOR,
                        '[class="header-search__input"]').send_keys(
                            "По ком звонит колокол", Keys.RETURN)
    res = driver.find_elements(By.CSS_SELECTOR,
                               '[class="product-card__caption"]')
    assert len(res) > 1


def test_number():
    driver.find_element(By.CSS_SELECTOR,
                        '[class="header-profile__button"]').click()
    driver.find_element(By.CSS_SELECTOR,
                        '[id="tid-input"]').send_keys("999999999")
    butt = driver.find_element(
        By.CSS_SELECTOR, '[class="app-button auth-modal__sms-button blue"]'
        ).value_of_css_property("background-color")
    butt_col = "rgb(44, 126, 220)"
    assert butt == butt_col


def test_searhh():
    driver.find_element(By.CSS_SELECTOR,
                        '[class="header-search__input"]').send_keys(
                            "孫子兵法", Keys.RETURN)
    res = driver.find_elements(By.CSS_SELECTOR,
                               '[class="product-card__caption"]')
    assert len(res) < 1


def test_add_to_card():
    driver.find_element(By.CSS_SELECTOR,
                        '[class="header-search__input"]').send_keys(
                            "По ком звонит колокол", Keys.RETURN)
    driver.find_element(By.CSS_SELECTOR,
                        '[class="chg-app-button chg-app-button--primary chg-app-button--s chg-app-button--brand-blue product-buttons__main-action product-buttons__main-action"]').click()
    icon = driver.find_element(By.CSS_SELECTOR, '[class="chg-indicator chg-indicator--bg-cherry chg-indicator--mod-m-l header-controls__indicator header-controls__indicator"]').is_displayed
    assert icon == "True"


def test_city():
    driver.find_element(By.CSS_SELECTOR,
                        '[class="header-city__title"]').click()
    driver.find_element(By.CSS_SELECTOR,
                        'class="button change-city__button change-city__button--cancel light-blue"').click()
    driver.find_element(
        By.CSS_SELECTOR,
        'class="city-modal__city-input"').send_keys("Новосибирск", Keys.RETURN)
    driver.find_element(By.CSS_SELECTOR, 'class="cities-list__item"').click()
    city = driver.find_element(By.CSS_SELECTOR,
                               'class="header-city__title"').text
    assert city == "Россия, Новосибирск"
