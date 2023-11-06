from src.item import Item


def test_init_all():
    items_1 = Item("Телефон", 7500, 3)
    items_3 = Item("Планшет", 5800, 1)
    items_4 = Item("Планшет", 9550, 2)
    assert len(Item.all) == 3


def test_calculate_total_price():
    items_1 = Item("Телефон", 7500, 3)
    items_2 = Item("Телефон", 5600, 7)
    assert items_1.calculate_total_price() == 22500
    assert items_2.calculate_total_price() == 39200


def test_apply_discount():
    items_3 = Item("Планшет", 5800, 1)
    items_4 = Item("Планшет", 9550, 2)
    Item.pay_rate = 0.6
    assert items_3.apply_discount() == 3480.0
    assert items_4.apply_discount() == 5730.0

