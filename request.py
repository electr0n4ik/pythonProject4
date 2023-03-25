
class Request:
    """
    Класс запроса
    """
    def __init__(self, string, store, shop):
        storages = {"склад": store, "магазин": shop}
        request = string.split()
        self._departure = storages[request[-3]]
        self._destination = storages[request[-1]]
        self._product = request[-5]
        self._amount = int(request[-6])

    @property
    def departure(self):
        return self._departure

    @property
    def destination(self):
        return self._destination

    @property
    def product(self):
        return self._product

    @property
    def amount(self):
        return self._amount
