from Warehouse import Warehouse;

def test_warehouse_one_book():
    order_cost = Warehouse([1], 1,1,1)
    assert order_cost == 3