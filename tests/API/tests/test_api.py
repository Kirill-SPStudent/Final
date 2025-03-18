import allure
from API.pages.cart import Cart
from API.pages.search import Search

Auth1 = ""


@allure.story("Корзина")
@allure.title("Добавление в корзину")
@allure.severity("Blocker")
def test_add_to_card():
    Url = "https://web-gate.chitai-gorod.ru/api"
    Crt = Cart(Url)
    res = Crt.add_to_card(
        "2444652", {"item_list_name": "search", "product_shelf": ""}, Auth1)
    assert res.status_code == 200


@allure.story("Корзина")
@allure.title("Изменение количества товара в корзине")
@allure.severity("Blocker")
def test_change_quan():
    Url = "https://web-gate.chitai-gorod.ru/api"
    Crt = Cart(Url)
    res = Crt.change_quantity("154773178", "2", Auth1)
    assert res.status_code == 200


@allure.story("Корзина")
@allure.title("Удаление товара из корзины")
@allure.severity("Blocker")
def test_delete_in_cart():
    Url = "https://web-gate.chitai-gorod.ru/api"
    Crt = Cart(Url)
    res = Crt.delete(Auth1, "154773178")
    assert res.status_code == 204


@allure.story("Поиск")
@allure.title("Поиск товара без названия")
@allure.description("Поле с названием товара пустое")
@allure.severity("Blocker")
def test_empty_name():
    Url = "https://web-gate.chitai-gorod.ru/api/v2/search/results"
    Srh = Search(Url)
    res = Srh.search("", 9, Auth1)
    assert res.status_code == 422


@allure.story("Поиск")
@allure.title("Поиск товара с невалидным значением результатов")
@allure.description("Количество показываемых результатов поиска меньше 0")
@allure.severity("Minor")
def test_neg_num_res():
    Url = "https://web-gate.chitai-gorod.ru/api/v2/search/results"
    Srh = Search(Url)
    res = Srh.search("1984", -19, Auth1)
    assert res.status_code == 422
