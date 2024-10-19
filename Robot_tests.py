from Robot import Robot;
from Tree import tree;
from Bin import Bin;

test_tree = tree(
    #     LL   L  LRL  LR   0  RL   R    
        [123, 12,  23, 45, 56, 67, 78], #ISBN
        [  1,  7,   3,  4,  7,  2,  9]  #Frequency 33 = total  split 23 and 11 
)
#####The movement pattern #######
    #move to root (1)  cost + 1
    #scan              cost + .5
    #retrive book      cost + .25
    #change direction  cost + 10
    #go back           cost + 1

def test_robot_can_give_cost_single_book():
    oneBookTree = tree (
        [10],   #ISBN
        [3]     #Frequency = 3
    )
    myRobot = Robot()
    myRobot.tree = oneBookTree
    answer = myRobot.costOfISBN(10)
    assert answer == 12.75

def test_robot_can_give_cost_book_left_of_root():
    myRobot = Robot()
    myRobot.tree = test_tree
    cost = myRobot.costOfISBN(12)
    assert cost == 15.25

def test_robot_can_give_cost_book_right_of_root():
    myRobot = Robot()
    myRobot.tree = test_tree
    cost = myRobot.costOfISBN(78)
    assert cost == 17.25