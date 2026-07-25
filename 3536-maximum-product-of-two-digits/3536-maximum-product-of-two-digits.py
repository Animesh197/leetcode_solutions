class Solution:
    def maxProduct(self, n: int) -> int:
        A = []
        for i in str(n):
            A.append(int(i))
        A.sort()
        return A[-1]*A[-2]
        