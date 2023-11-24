from src.item import Item


class MixinLog:
    def __init__(self):
        """ Инициализация доступных языков"""
        self.languages = ['EN', 'RU']

    def get_lang(self):
        """ Функция возвращает список с доступными языками """
        return self.languages


class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        """ Инициализация с наследованием от класса Item и MixinLog,
        language по умолчанию EN """
        super().__init__(name, price, quantity)
        self.mixin = MixinLog().get_lang()
        self.__language = self.mixin[0]

    @property
    def language(self):
        """ Декоратор для чтения атрибута language """
        return self.__language

    def change_lang(self):
        """ Метод для переключения языка EN -> RU -> EN """
        if self.__language == self.mixin[1]:
            self.__language = self.mixin[0]
            return self.__language
        if self.__language == self.mixin[0]:
            self.__language = self.mixin[1]
            return self.__language

    def __str__(self):
        """ Возвращает название товара """
        return self.name
