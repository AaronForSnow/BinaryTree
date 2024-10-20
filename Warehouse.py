from Robot import Robot;
from Tree import tree;

def Warehouse(frequencies,  move_once, scan, turn_around):
    ## takes in array of frequencies
    # makes array of isbns
    isbns = []
    for i in range(len(frequencies)):
        isbns.append(i)
    # makes tree from two arrays
    _tree = tree(isbns, frequencies)
    # makes robot with tree
    robot = Robot(_tree, move_once, scan, turn_around)
    # calls cost for each isbn frequency times
    total = 0
    for i in range(len(frequencies)):
        b_r_c = robot.costOfISBN(isbns[i])
        total += b_r_c * frequencies[i]
    return total

