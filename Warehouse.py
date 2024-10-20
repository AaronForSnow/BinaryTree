from Robot import Robot;
from Tree import tree;

class Warehouse:
    def __init__(self, frequencies,  move_once, scan, turn_around):
        ## takes in array of frequencies
        # makes array of isbns
        isbns = []
        for i in len(frequencies):
            isbns.append(i)
        # makes tree from two arrays
        tree = tree(frequencies, isbns)
        # makes robot with tree
        # calls cost for each isbn frequency times
        # returns total

        return

