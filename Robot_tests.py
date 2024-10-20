from Robot import Robot;
from Tree import tree;
from Bin import Bin;
#####The movement pattern #######
    #move 1 * distance  cost + 1 * abs(current - target)
    #scan              cost + .5
    #retrive book      cost + .25
    #change direction  cost + 10
    #go back           cost + 1

test_tree = tree(
    #     LL    L   LRL   LR    0   RL    R    
        [123, 124,  125, 126, 127, 128, 129], #ISBN
        [  1,   7,    3,   4,   7,   2,   9]  #Frequency 33 = total  split 23 and 11 
)
move_once = 1
scan = .5
turn_around = 10

def test_robot_can_not_give_cost_Bad_ISBN():
    myRobot = Robot(test_tree,move_once, scan, turn_around)
    cost = myRobot.costOfISBN(0)
    assert cost == "no ISBN of that Value"

def test_robot_can_give_cost_single_book():
    oneBookTree = tree (
        [10],   #ISBN
        [3]     #Frequency = 3
    )
    myRobot = Robot(oneBookTree,move_once, scan, turn_around)
    answer = myRobot.costOfISBN(10)
    assert answer == 12.50

### Tests may be in an infinite loop...

def test_robot_can_give_cost_book_left_of_root():
    myRobot = Robot(test_tree,move_once, scan, turn_around)
    cost = myRobot.costOfISBN(124)
    assert cost == 15

def test_robot_can_give_cost_book_right_of_root():
    myRobot = Robot(test_tree,move_once, scan, turn_around)
    cost = myRobot.costOfISBN(129)
    assert cost == 17

def test_robot_can_give_cost_book_Left_Left_of_root():
    myRobot = Robot(test_tree,move_once, scan, turn_around)
    cost = myRobot.costOfISBN(123)
    assert cost == 19.50

def test_robot_can_give_cost_book_Left_Right_of_root():
    myRobot = Robot(test_tree,move_once, scan, turn_around)
    cost = myRobot.costOfISBN(126)
    assert cost == 21.50
