import requests
import pytest
import allure

Auth1 = ""


def test_add_to_card():
    base_url = "https://web-gate.chitai-gorod.ru/api/v1/cart/product"

    creds = {"id": 2444652,
             "adData": {"item_list_name": "search", "product_shelf": ""}}
    my_headers = {'Authorization': Auth1}

    res = requests.post(base_url, json=creds, headers=my_headers)
    assert res.status_code == 200


def test_change_quan():
    base_url = "https://web-gate.chitai-gorod.ru/api/v1/cart"

    creds = [{"id": 154773178, "quantity": 2}]

    my_headers = {'Authorization': Auth1}

    res = requests.put(base_url, json=creds, headers=my_headers)
    assert res.status_code == 200


def test_delete_in_cart():
    base_url = "https://web-gate.chitai-gorod.ru/api/v1/cart/product/154773178"

    creds = {}

    my_headers = {'Authorization': Auth1}
    res = requests.delete(base_url, json=creds, headers=my_headers)

    assert res.status_code == 204


def test_empty_name():
    base_url = "https://web-gate.chitai-gorod.ru/api/v2/search/results"

    creds = {"searchPhrase": "", "resultCount": 8}

    my_headers = {'Authorization': Auth1}
    res = requests.delete(base_url, json=creds, headers=my_headers)

    assert res.status_code == 422


def test_neg_num_res():
    base_url = "https://web-gate.chitai-gorod.ru/api/v2/search/results"

    creds = {"searchPhrase": "Война и Мир", "resultCount": -10}

    my_headers = {'Authorization': Auth1}
    res = requests.delete(base_url, json=creds, headers=my_headers)

    assert res.status_code == 422
