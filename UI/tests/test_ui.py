import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from UI.pages.main import MainPage
from UI.pages.Account import Account
from UI.pages.Geolocation import Geoloc


@allure.story("Поиск")
@allure.title("Поиск товара по валидному названию")
@allure.description("Поле с названием товара на русском языке")
@allure.severity("Blocker")
def test_seacrh_pos():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    with allure.step("Ввод названия товара на русском языке"):
        Main.searchfild("По ком звонит колокол")
    with allure.step("Проверка, что количесто найденных товаров больше 0"):
        assert len(Main.product_description) > 0


@allure.story("Поиск")
@allure.title("Поиск товара по невалидному названию")
@allure.description("Поле с названием товара на китайском языке")
@allure.severity("Critical")
def test_search_neg():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    with allure.step("Ввод названия товара на китайском языке"):
        Main.searhfild("孫子兵法")
    with allure.step("Проверка, что количесто найденных товаров меньше 1"):
        assert len(Main.product_description) < 1


@allure.story("Аккаунт")
@allure.title("Вход в аккаунт")
@allure.description("Ввод номера телефона")
@allure.severity("Blocker")
def test_number():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Acc = Account(driver)
    with allure.step("Ввод номера телефона, исключая первые цифры (+79)"):
        Acc.input_number_profile("9999999999")
    with allure.step("Проверка цвета кнопки 'Получить код'"):
        color1 = Acc.color_button_in_profile()
    color2 = "rgb(44, 126, 220)"
    with allure.step("Проверка, цвета кнопки получения кода при вводе номера с цветом этой кнопки по документации"):
        assert color1 == color2


@allure.story("Корзина")
@allure.title("Добавление товара в корзину")
@allure.description("Проверка появления значка с единицей на иконке корзины на странице поиска товара")
@allure.severity("Blocker")
def test_add_to_carf():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Main = MainPage(driver)
    Main.searchfild("По ком звонит колокол")
    Main.add_to_card()
    icon = Main.icon_on_card()
    with allure.step("Проверка, что цифра '1' появляется на иконке корзины"):
        assert icon == "True"


@allure.story("Геолокация")
@allure.title("Изменение геолокации")
@allure.description("Изменение города в левом верхнем углу главной страницы")
@allure.severity("Blocker")
def test_change_city():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    Geo = Geoloc(driver)
    Town = "Новосибирск"
    Geo.change_city(Town)
    with allure.step("Проверка, что вводимый ранее город отображается в левом верхнем углу страницы"):
        assert Geo.city == Town
