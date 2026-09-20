from bisect import bisect_right
class Solution:
    def maximumTotalDamage(self, power):
        freq = {}
        for x in power:
            freq[x] = freq.get(x, 0) + 1

        nums = sorted(freq)
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            x = nums[i - 1]
            skip = dp[i - 1]

            j = bisect_right(nums, x - 3)
            take = dp[j] + x * freq[x]
            dp[i] = max(skip, take)

        return dp[n]