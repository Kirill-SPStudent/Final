import requests


class Search():
    def __init__(self, url):
        self.url = url

    def search(self, searchPhrase: str, resultCount: int, Authorization: str):
        """Ввод названия товара и ввод количества полученных результатов"""
        body = {searchPhrase: "", resultCount: ""}
        head = {Authorization: ""}
        res = requests.delete(self.url, json=body, headers=head)
        return res
