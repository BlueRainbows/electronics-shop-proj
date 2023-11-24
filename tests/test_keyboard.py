from src.keyboard import MixinLog, Keyboard


def test_MixinLog():
    """ Тест проверяет что класс миксинлог возвращает список """
    mixin = MixinLog()
    assert type(mixin.get_lang()) == list


def test_keyboard():
    """ Тест проверяет что атрибут language является строкой,
    По умолчанию он равен EN, функция для переключения языка работает исправно
    Длина наименования товара выводиться исправно """
    keyboards = Keyboard('Dark Project KD87A', 9600, 5)
    assert type(keyboards.language) == str
    assert keyboards.language != 'RU'
    keyboards.change_lang()
    assert keyboards.language == 'RU'
    assert len(str(keyboards)) == 18

