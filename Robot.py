# this is where the robot will have a tree and be given a list of ISBN's to find 
# and calulate the cost of collecting the books
from Tree import tree;
class Robot:
    
    def __init__(self):
        self.tree = None
        self.move_once_cost = 1
        self.scan_cost = .5
        self.retrieve_cost = .25
        self.change_direction_cost = 10
        self.return_to_start_cost = 1
        return
    def costToMoveAndScan(self, currentPosition, targetPosition):
        moveCost = (targetPosition - currentPosition) * self.move_once_cost
        scanCost = .5
        return moveCost + scanCost
    def costOfISBN(self, isbn):
        found = False
        cost = self.move_once_cost #because bin 0 is 1 away from the robot's starting place
        i = 0
        while not found:
            if (self.tree.bins[i].Isbn) == isbn:
                cost += self.scan_cost
                cost += self.retrieve_cost
                found = True
                print ("found book at i = ", i)
            #isbn was too big, go left
            elif (self.tree.bins[i].Isbn > isbn):
                cost += self.costToMoveAndScan(i, 2*i )
                i = 2 * i
                print ("i now equals ", i)
            #isbn was too small, go right
            elif (self.tree.bins[i].Isbn < isbn):
                cost += self.costToMoveAndScan(i, 2*i + 1)
                i = 2 * i + 1
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