class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()

        reach = 0
        i = 0
        added = 0

        while reach < target:
            if i < len(coins) and coins[i] <= reach + 1:
                reach += coins[i]
                i += 1
            else:
                added += 1
                reach += reach + 1

        return added