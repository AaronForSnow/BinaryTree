# this is where the robot will have a tree and be given a list of ISBN's to find 
# and calulate the cost of collecting the books
from Tree import tree;
class Robot:
    
    def __init__(self, tree, move_once, scan, turn_around):
        self.tree = tree
        self.move_once_cost = move_once # constant alfa
        self.scan_cost = scan     # constant beta
        self.retrieve_cost = 0  # constant ... we din't need
        self.change_direction_cost = turn_around # constant gama
        return
    def costToMove(self, currentPosition, targetPosition):
        moveCost = abs(targetPosition - currentPosition) * self.move_once_cost
        return moveCost
    def costOfISBN(self, isbn):
        found = False
        cost = self.move_once_cost #because bin 0 is 1 away from the robot's starting place
        i = 1
        current_bin = self.tree.root_bin
        try:
            while not found:
                cost += self.scan_cost
                if (current_bin.Isbn) == isbn:
                    cost += self.retrieve_cost
                    found = True
                    print ("found book at i = ", i)
                #isbn was too big, go left
                elif (current_bin.Isbn > isbn):
                    if current_bin.Left == None:
                        return "no ISBN of that Value"
                    current_bin = current_bin.Left
                    cost += self.costToMove(i, 2*i)
                    i = 2 * i
                    print ("i now equals ", i, current_bin.Isbn)
                #isbn was too small, go right
                elif (current_bin.Isbn < isbn):
                    if current_bin.Right == None:
                        return "no ISBN of that Value"
                    current_bin = current_bin.Right
                    cost += self.costToMove(i, 2*i + 1)
                    i = 2 * i + 1
                    print ("i now equals ", i, current_bin.Isbn)
        except Exception as e:
            Found = True
            print ("error!!! isbn evaluated to ",current_bin.Isbn, " and i was ", i)
            print (e)     
        # now, add to it the cost to turn around and come back, and traverse to that.
        cost += self.change_direction_cost #change directions
        cost += self.costToMove(i, 0) #come back to bin 0
        print ("Total cost was:",cost)
        return cost
            
        
        #check index 1
        #if index 1 == isbn, return value
        #if index 1 < isbn, cost = cost at this point + CostOfISBN(left)