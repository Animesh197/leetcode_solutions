class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]

    def add(self, num):
        if num == 0:
            self.pre = [1]
        else:
            self.pre.append(self.pre[-1] * num)

    def getProduct(self, k):
        if k >= len(self.pre):
            return 0

        return self.pre[-1] // self.pre[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)