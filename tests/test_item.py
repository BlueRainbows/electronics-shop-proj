"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init_all():
    """ Тест на длинну добавленных экземпляров """
    items_1 = Item("Телефон", 7500, 3)
    items_3 = Item("Планшет", 5800, 1)
    items_4 = Item("Планшет", 9550, 2)
    assert len(Item.all) == 3


def test_calculate_total_price():
    """ Тест на точность подсчёта данных общей стоимости товара в наличии """
    items_1 = Item("Телефон", 7500, 3)
    items_2 = Item("Телефон", 5600, 7)
    assert items_1.calculate_total_price() == 22500
    assert items_2.calculate_total_price() == 39200


def test_apply_discount():
    """ Тест на точность подсчёта данных скидки на товар """
    items_3 = Item("Планшет", 5800, 1)
    items_4 = Item("Планшет", 9550, 2)
    Item.pay_rate = 0.6
    assert items_3.apply_discount() == 3480.0
    assert items_4.apply_discount() == 5730.0


def test_len_name():
    """ Тест на подсчёт длинны наименования """
    item_5 = Item('Планшет', 15000, 5)
    item_5.name = 'УльтраплоскийПланшет'
    assert len(item_5.name) == 10
