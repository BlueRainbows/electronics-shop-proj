from src.phone import Phone


def test_init_Phone():
    """ Тест на правильность передачи инициализации от родительского класса """
    phones2 = Phone("iPhone 14", 12000, 2, 3)
    assert phones2.price == 12000


def test_number_of_sim():
    """ Тест на правильность сеттера """
    phones1 = Phone("iPhone 14", 120_000, 5, 7)
    phones1.number_of_sim = 0
    assert phones1.number_of_sim != 0


def test_mag_met():
    """ Тесты проверяющие магические методы на правильность вывода """
    phones3 = Phone('Mobile_Android', 10000, 10, 1)
    assert repr(phones3) == "Phone('Mobile_Android', 10000, 10, 1)"
    assert type(repr(phones3)) == str
    assert len(str(phones3)) == 14

