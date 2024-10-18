# this is where the robot will have a tree and be given a list of ISBN's to find 
# and calulate the cost of collecting the books
class Robot:
    def __init__(self):
        tree = None
        return
    def CostOfISBN(self, isbn):
        #check index 1
        #if index 1 == isbn, return value
        #if index 1 < isbn, cost = cost at this point + CostOfISBN(left)
        return 0