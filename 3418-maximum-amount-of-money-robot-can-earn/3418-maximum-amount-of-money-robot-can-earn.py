class Solution:
    def maximumAmount(self, coins):
        m = len(coins)
        n = len(coins[0])
        neg = float('-inf')

        dp = [[neg] * 3 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                x = coins[i][j]
                curr = [neg] * 3

                if i == 0 and j == 0:
                    curr[0] = x

                    if x < 0:
                        curr[1] = 0

                    dp[j] = curr
                    continue

                up = dp[j]
                left = dp[j - 1] if j > 0 else [neg] * 3

                for k in range(3):
                    best = max(up[k], left[k])

                    if best != neg:
                        curr[k] = best + x

                if x < 0:
                    for k in range(1, 3):
                        best = max(up[k - 1], left[k - 1])

                        if best != neg:
                            curr[k] = max(curr[k], best)

                dp[j] = curr

        return max(dp[n - 1])
        