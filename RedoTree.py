from Bin import Bin

class RedoTree:
    def __init__ (self, isbns, frequencies): #Isbns are already in order!
        self.isbns = isbns,
        self.frequencies = frequencies
        #we set the tree here
        self.root_bin = self.create_optimal_tree(isbns, frequencies)
        #self.root_bin, lefts, rights = self.get_root_bin(target_frequency, self.Bins)

    def create_optimal_tree(self, isbns, frequencies):
        if (len(isbns) == 0):
            return None
        elif(len(isbns) == 1):
            myBin = Bin(isbns[0], frequencies[0])
            myBin.Left = None
            myBin.Right = None
            return myBin
        