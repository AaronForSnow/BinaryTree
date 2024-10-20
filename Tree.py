from Bin_tests import Bin;

class tree:
    def __init__ (self, isbns, frequencies): #Isbns are already in order!
        self.total_frequency = 0
        self.Bins = []
        for i in range(len(frequencies)):
            self.total_frequency += frequencies[i]
            b = Bin(isbns[i], frequencies[i])
            self.Bins.append(b)
        target_frequency = self.total_frequency/2
        self.root_bin, lefts, rights = self.get_root_bin(target_frequency, self.Bins)
        self.set_tree(lefts, rights, self.root_bin)

    def set_tree(self, lefts, rights, root):
        if (lefts):
            target = 0
            for i in range(len(lefts)):
                target += lefts[i].Frequency
            target = target/2
            l, lefters, righters = self.get_root_bin(target,lefts)
            self.set_tree(lefters, righters, l)
            root.set_Left(l)
        if (rights):
            target = 0
            for i in range(len(rights)):
                target += rights[i].Frequency
            target = target/2
            r, lefters, righters = self.get_root_bin(target,rights)
            self.set_tree(lefters, righters, r)
            root.set_Right(r)

    def get_root_bin(self, target, sub_bins):
        count = 0
        for i in range(len(sub_bins)):
            count += sub_bins[i].Frequency
            if count >= target:
                return sub_bins[i], sub_bins[:i], sub_bins[i+1:]

    def set_bins_in_hash_order(self):
        return 

