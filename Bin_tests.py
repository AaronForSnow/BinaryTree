from Bin import Bin;

def test_bin_set_left():
    my_bin = Bin(123, 7)
    l = Bin(1234, 3)
    my_bin.set_Left(l)
    assert my_bin.Left == l

def test_get_frequency_for_bin_with_one_node_returns_own_frequency():
    my_bin = Bin(100000, 10)
    assert my_bin.get_total_frequency() == 10

def test_get_frequency_for_bin_with_self_node_and_right_node_returns_correct_frequency():
    my_bin = Bin(100000, 10)
    right_bin = Bin(123, 2)
    my_bin.Right = right_bin
    assert my_bin.get_total_frequency() == 12

def test_get_frequency_for_bin_with_many_nodes_returns_correct_frequency():
    my_bin = Bin(100000, 10)
    right_bin = Bin(123, 2)
    my_bin.Right = right_bin
    left_bin = Bin(12, 1)
    my_bin.Left = left_bin
    llbin = Bin(1234, 10)
    left_bin.Left = llbin
    assert my_bin.get_total_frequency() == 23