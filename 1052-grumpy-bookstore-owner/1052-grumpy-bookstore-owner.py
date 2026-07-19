class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        best = extra

        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra += customers[i]

            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            best = max(best, extra)

        return satisfied + best