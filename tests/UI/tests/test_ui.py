import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from UI.pages.main import MainPage
from UI.pages.Account import Account
from UI.pages.Geolocation import Geoloc


@allure.story("Поиск")
@allure.severity
def test_seacrh_pos():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    Main.searchfild("По ком звонит колокол")
    assert len(Main.product_description) > 1


@allure.story("Поиск")
@allure.severity
def test_search_neg():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    Main.searhfild("孫子兵法")
    assert len(Main.product_description) < 1


@allure.story("Аккаунт")
@allure.severity
def test_number():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Acc = Account(driver)
    Acc.input_number_profile("9999999999")
    color1 = Acc.color_button_in_profile()
    color2 = "rgb(44, 126, 220)"
    assert color1 == color2


@allure.story("Корзина")
@allure.severity
def test_add_to_carf():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    Main.searhfild("По ком звонит колокол")
    Main.add_to_card()
    icon = Main.icon_on_card()
    assert icon == "True"


@allure.story("Геолокация")
@allure.severity
def test_change_city():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Geo = Geoloc(driver)
    Town = "Новосибирск"
    Geo.change_city(Town)
    assert Geo.city == Town
