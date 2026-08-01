class RLEIterator:

    def __init__(self, encoding):
        self.encoding = encoding
        self.i = 0

    def next(self, n):
        while self.i < len(self.encoding):
            if self.encoding[self.i] < n:
                n -= self.encoding[self.i]
                self.encoding[self.i] = 0
                self.i += 2
            else:
                self.encoding[self.i] -= n
                return self.encoding[self.i + 1]

        return -1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)