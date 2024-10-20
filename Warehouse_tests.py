from Warehouse import Warehouse;

def test_warehouse_one_book():
    frequencies = [1]
    order_cost = Warehouse(frequencies,1,1,1)
    # move once, scan, turn_around, move_once = 4
    assert order_cost == 4

def test_warehouse_two_books():
    frequencies = [1,2]
    order_cost = Warehouse(frequencies,1,1,1)
    # move once, scan, turn_around, move_once = 4
    # move once, scan, move_again, scan, turn_around, move_twice = 7
    # 7 + 4(2) = 15
    assert order_cost == 15

def test_warehouse_seven_books():
              #     LL    L   LRL   LR    0   RL    R 
    frequencies = [  1,   7,    3,   4,   7,   2,   9]
            #        4    2    10    5    1    6    3  Distance from start
    # 0 L R LL LR RL RR LLL LLR LRL LRR RLL RLR RRL RRR  
    # 1 2 3  4  5  6  7   8   9  10  11  12  13  14  16 Indexes
    # 7 7 9  1  4  2  _   _   _   3   _   _   _   _   _ Placements
    order_cost = Warehouse(frequencies,1,1,1)
    # move_cost 4*2(return) + scan 3 + turn_around 1= 12
    # move_cost 2*2(return) + scan 2 + turn_around 1= 7
    # move_cost 10*2(return) + scan 4 + turn_around 1= 25
    # move_cost 5*2(return) + scan 3 + turn_around 1= 14
    # move_cost 1*2(return) + scan 1 + turn_around 1= 4
    # move_cost 6*2(return) + scan 3 + turn_around 1= 16
    # move_cost 3*2(return) + scan 2 + turn_around 1= 9
    # 12*1 + 7*7 + 25*3 + 14*4 + 4*7 + 16*2 + 9*9 = 333
    assert order_cost == 333