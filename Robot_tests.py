from Robot import Robot;
from Tree import tree;
from Bin import Bin;

test_tree = tree(
    #     LL    L   LRL   LR    0   RL    R    
        [123, 124,  125, 126, 127, 128, 129], #ISBN
        [  1,   7,    3,   4,   7,   2,   9]  #Frequency 33 = total  split 23 and 11 
)

def test_robot_can_give_cost_single_book():
    #move to root (1)  cost + 1
    #scan              cost + .5
    #retrive book      cost + .25
    #change direction  cost + 10
    #go back           cost + 1
    assert False