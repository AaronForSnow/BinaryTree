#def test_get_root_of_empty_array_returns_null():
    # our tree just has an array of frequencies

import RedoTree

def test_can_create_tree():
    my_tree = RedoTree.RedoTree(
            [], #ISBN
            []  #Frequency
        )
    assert my_tree.root_bin  == None

