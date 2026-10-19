class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 2

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j].get(d, 1) + 1
                ans = max(ans, dp[i][d])

        return ans