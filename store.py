from storage import Storage


class Store(Storage):
    """
    Класс склада
    """
    def __init__(self, items=None, capacity=200):
        if items is None:
            items = {}
        self._items = items
        self._capacity = capacity

    def __repr__(self):
        return 'склад'

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, name, qnt):
        if self._get_free_space() < qnt:
            print("Не хватает места на складе")
            return False
        else:
            self._items[name] = self._items[name] + qnt
            return True

    def remove(self, name, qnt):
        if self._items[name] < qnt:
            print("На складе недостаточно товаров")
            return False
        else:
            self._items[name] = self._items[name] - qnt
            return True

    def _get_free_space(self):
        return self._capacity - sum(self._items.values())

    def get_items(self):
        print('На складе хранится:')
        for name, qnt in self._items.items():
            print(f'{qnt} {name}')
        print('\n')

    def _get_unique_items_count(self):
        return len(self._items)
