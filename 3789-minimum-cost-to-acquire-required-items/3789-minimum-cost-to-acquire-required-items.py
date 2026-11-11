class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2

        common = min(need1, need2)
        ans = common * costBoth

        if need1 > need2:
            ans += min(cost1, costBoth) * (need1 - need2)
        else:
            ans += min(cost2, costBoth) * (need2 - need1)

        return ans