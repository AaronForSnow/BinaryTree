#def test_get_root_of_empty_array_returns_null():
    # our tree just has an array of frequencies
from Bin import Bin
from RedoTree import RedoTree


def test_can_create_empty_tree():
    my_tree = RedoTree(
            [], #ISBN
            []  #Frequency
        )
    assert my_tree.root_bin  == None

def test_can_create_tree_with_only_one_isbn():
    my_tree = RedoTree(
            [12], #ISBN
            [2]  #Frequency
    )
    assert my_tree.root_bin.Frequency == 2
    assert my_tree.root_bin.Isbn == 12
    assert my_tree.root_bin.Left == None
    assert my_tree.root_bin.Right == None

def test_can_create_tree_with_only_one_isbn():
    my_tree = RedoTree(
            [12, 13], #ISBN
            [2, 37]  #Frequency
    )
    assert my_tree.root_bin.Frequency == 37
    assert my_tree.root_bin.Isbn == 13
    assert my_tree.root_bin.Left.Isbn == 12
    assert my_tree.root_bin.Left.Frequency == 2
    assert my_tree.root_bin.Right == None
