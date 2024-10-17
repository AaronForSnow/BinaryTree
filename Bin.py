class Bin:
    def __init__(self, isbn, frequency):
        self.Isbn = isbn
        self.Frequency = frequency
        self.Left = None
        self.Right = None
    def set_Left(self, bin):
        self.Left = bin
    def set_Right(self, bin):
        self.Right = bin
    def get_total_frequency(self):
        leftFrequency = 0
        if (self.Left):
            leftFrequency = self.Left.get_total_frequency()
        rightFrequency = 0
        if (self.Right):
            rightFrequency = self.Right.get_total_frequency()
        return self.Frequency + leftFrequency + rightFrequency
    