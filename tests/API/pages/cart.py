import requests


class Cart():

    def __init__(self, url):
        self.url = url

    def add_to_card(self, id: int, adData: dict, Authorization: str):
        """Добавление товара в корзину"""
        body = {id: "", adData: {}}
        head = {Authorization: ""}
        res = requests.post(
            self.url+'/v1/cart/product', json=body, headers=head)
        return res

    def change_quantity(self, id: int, quantity: int, Authorization: str):
        """Изменение количества товара в корзине"""
        body = {id: "", quantity: ""}
        head = {Authorization: ""}
        res = requests.put(self.url+'/v1/cart', json=body, headers=head)
        return res

    def delete(self, Authorization: str, term: int):
        """Удаление товара из корзины"""
        id = term
        body = {}
        head = {Authorization: ""}
        res = requests.delete(self.url+'/v1/cart/'+id, json=body, headers=head)
        return res
