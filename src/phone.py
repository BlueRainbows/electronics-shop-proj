from src.item import Item


class Phone(Item):
    def __init__(self,  name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """ Декоратор property """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """ Сеттер, проверяющий значение number_of_sim
        Если number_of_sim больше 0, то значение возвращается,
        Иначе number_of_sim равен ошибке и выводит ответ об ошибке на экран """
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        elif number_of_sim <= 0:
            self.__number_of_sim = ValueError
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name
