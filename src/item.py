class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        """
        Декоратор property.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер обрезающий длину наименования, если она превышает 10 символов.
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, который принимает путь к документу с значениями.
        Открывает документ и преобразовывает его в словарь.
        Инициализирует значения под атрибуты класса
        """
        import csv
        cls.all.clear()
        with open(path, 'r', newline='') as attributes:
            attribute = csv.DictReader(attributes)
            for attr in attribute:
                name = attr['name'],
                price = cls.string_to_number(attr['price'])
                quantity = cls.string_to_number(attr['quantity'])
                items_csv = Item(name, price, quantity)
            return items_csv

    @staticmethod
    def string_to_number(string: str):
        """
        Метод принимает строковое значение числа и переводит его в целое число
        """
        if string.isdigit:
            if '.' in string:
                string = int(float(string))
            else:
                string = int(string)
            return string
