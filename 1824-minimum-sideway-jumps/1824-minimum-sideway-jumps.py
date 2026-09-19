class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        dp = [1, 0, 1]

        for i in range(1, len(obstacles)):
            obstacle = obstacles[i]

            if obstacle:
                dp[obstacle - 1] = float('inf')

            for j in range(3):
                if j != obstacle - 1:
                    dp[j] = min(dp[j], dp[(j + 1) % 3] + 1, dp[(j + 2) % 3] + 1)

        return min(dp)