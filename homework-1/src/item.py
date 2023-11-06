class Item:
    pay_rate = 1
    all = []

    def __init__(self, product, price, quantity):
        """ Функция инициализирует атрибуты класса и добавляет их значения в список """
        self.product = product
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        """ Функция делает общий расчёт стоимости товара """
        return self.price * self.quantity

    def apply_discount(self):
        """ Функция делает расчёт скидки для конкретного товара """
        self.price = self.price * self.pay_rate
        return self.price

