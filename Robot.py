# this is where the robot will have a tree and be given a list of ISBN's to find 
# and calulate the cost of collecting the books
from Tree import tree;
class Robot:
    def __init__(self):
        self.tree = None
        return
    def costToMoveAndScan(self, currentPosition, targetPosition):
        moveCost = targetPosition - currentPosition
        scanCost = .5
        return moveCost + scanCost
    def costOfISBN(self, isbn):
        found = False
        cost = 0.0
        i = 0
        while not found:
            if (self.tree.bins[i].Isbn) == isbn:
                #scan book
                cost += 0.5
                #retrieve book
                cost += 0.25
                found = True
            elif (self.tree.bins[i].Isbn < isbn):
                cost += self.costToMoveAndScan(i, 2**i)
                i = 2 **i
        #now, add to it the cost to turn around and come back, and traverse to that.
        cost += 10 #change directions
        cost += i #come back to bin 0
        cost += 1 #come back one more
        print (cost)
        return cost
            
        
        #check index 1
        #if index 1 == isbn, return value
        #if index 1 < isbn, cost = cost at this point + CostOfISBN(left)