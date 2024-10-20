from Tree import tree;
from Bin_tests import Bin;

## Set_sub_Root TESTS
## 0 = root, L = left child  R = right child  RL = Right child's Left child ect
def test_Set_Sub_Root_double():
    my_tree = tree(
        #      L   0
            [123, 12], #ISBN
            [  1,  7]  #Frequency
        )
    assert my_tree.root_bin.Left.Frequency == Bin(123, 1).Frequency
    assert my_tree.root_bin.Left.Isbn == Bin(123, 1).Isbn

def test_Set_Sub_Root_triple():
    my_tree = tree(
        #      L   0   R
            [123, 12, 23], #ISBN
            [  1,  7,  3]  #Frequency
        )
    assert my_tree.root_bin.Left.Frequency == Bin(123, 1).Frequency
    assert my_tree.root_bin.Left.Isbn == Bin(123, 1).Isbn
    assert my_tree.root_bin.Right.Frequency == Bin(23, 3).Frequency
    assert my_tree.root_bin.Right.Isbn == Bin(23, 3).Isbn

def test_Set_Sub_Root_seven():
    my_tree = tree(
        #     LL   L  LRL  LR   0  RL   R    
            [123, 12,  23, 45, 56, 67, 78], #ISBN
            [  1,  7,   3,  4,  7,  2,  9]  #Frequency 33 = total  split 23 and 11 
        )
    assert my_tree.root_bin.Left.Frequency == Bin(12, 7).Frequency
    assert my_tree.root_bin.Left.Isbn == Bin(12, 7).Isbn
    assert my_tree.root_bin.Right.Frequency == Bin(78, 9).Frequency
    assert my_tree.root_bin.Right.Isbn == Bin(78, 9).Isbn
    assert my_tree.root_bin.Left.Right.Left.Frequency == Bin(23, 3).Frequency
    assert my_tree.root_bin.Left.Right.Left.Isbn == Bin(23, 3).Isbn

## Set_Root_Bin TESTS
def test_Set_root_bin_single():
    my_tree = tree(
            [123],  #ISBN
            [1] #Frequency
        )
    assert my_tree.root_bin.Frequency == Bin(123, 1).Frequency
    assert my_tree.root_bin.Isbn == Bin(123, 1).Isbn

def test_Set_root_bin_double():
    my_tree = tree(
            [123, 12], #ISBN
            [  1,  7]  #Frequency
        )
    assert my_tree.root_bin.Frequency == Bin(12, 7).Frequency
    assert my_tree.root_bin.Isbn == Bin(12, 7).Isbn

def test_Set_root_bin_Triple():
    my_tree = tree(
            [123, 12, 23], #ISBN
            [  1,  7,  3]  #Frequency
        )
    assert my_tree.root_bin.Frequency == Bin(12, 7).Frequency
    assert my_tree.root_bin.Isbn == Bin(12, 7).Isbn

def test_Set_root_bin_Seven():
    my_tree = tree(
            [123, 12, 23, 45, 56, 67, 78], #ISBN
            [  1,  7,  3,  4,  7,  2,  9]  #Frequency 33 = total  split 23 and 11 
        )
    assert my_tree.root_bin.Frequency == Bin(56, 7).Frequency
    assert my_tree.root_bin.Isbn == Bin(56, 7).Isbn

# ## Tests For Hashing of Bins
# def test_root_bin_two():
#     my_tree = tree(
#         #      L   0
#             [123, 12], #ISBN
#             [  1,  7]  #Frequency
#         )
#     # root starts at bins[1] because Bins[0] == the delivory box the robot starts at. (also easier for hashing math)
#     assert my_tree.Bins[1].Frequency == Bin(12, 7).Frequency
#     assert my_tree.Bins[1].Isbn == Bin(12, 7).Isbn
