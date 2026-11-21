import random
from bisect import bisect_left

class Solution:

    def __init__(self, w):
        self.pre = []
        total = 0

        for x in w:
            total += x
            self.pre.append(total)

        self.total = total

    def pickIndex(self):
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)