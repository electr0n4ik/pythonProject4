from store import Store
from shop import Shop
from request import Request


def main():
    """
    Выполнение запроса пользователя для доставки
    """
    items = {"яблоки": 4, "бананы": 10, "груши": 6}
    store = Store(items)
    shop = Shop()

    store.get_items()
    shop.get_items()

    # Пример запроса: "Доставить 3 бананы из склад в магазин", на складе останется 7 бананов
    while True:
        user_string = input("Введите запрос: ")
        if user_string == 'стоп':
            break

        request = Request(user_string, store, shop)
        departure = request.departure
        destination = request.destination
        amount = request.amount
        product = request.product

        if departure.remove(product, amount):
            print(f'Курьер забрал {amount} {product} из {departure}\n'
                  f'Курьер везет {amount} {product} из {departure} в {destination}')
            if destination.add(product, amount):
                print(f'Курьер доставил {amount} {product} в {destination}')
                destination.get_items()
                departure.get_items()


if __name__ == '__main__':
    main()
