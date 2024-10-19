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
        cost = 1.0 #because bin 0 is 1 away from the robot's starting place
        i = 0
        while not found:
            if (self.tree.bins[i].Isbn) == isbn:
                #scan book
                cost += 0.5
                #retrieve book
                cost += 0.25
                found = True
                print ("found book at i = ", i)
            #isbn was too big, go left
            elif (self.tree.bins[i].Isbn > isbn):
                cost += self.costToMoveAndScan(i, 2*i + 1)
                i = 2 * i + 1
                print ("i now equals ", i)
            #isbn was too small, go right
            elif (self.tree.bins[i].Isbn < isbn):
                cost += self.costToMoveAndScan(i, 2*i + 2)
                i = 2 * i + 2
                print ("i now equals ", i)
            else:
                Found = True
                print ("error!!! isbn evaluated to ", self.tree.bins[i].Isbn, " and i was ", i)
            
        #now, add to it the cost to turn around and come back, and traverse to that.
        cost += 10 #change directions
        cost += i #come back to bin 0
        cost += 1 #come back one more
        print (cost)
        return cost
            
        
        #check index 1
        #if index 1 == isbn, return value
        #if index 1 < isbn, cost = cost at this point + CostOfISBN(left)