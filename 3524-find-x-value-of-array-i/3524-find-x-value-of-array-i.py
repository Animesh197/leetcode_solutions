class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k

        for x in nums:
            x %= k
            curr = [0] * k

            curr[x] += 1

            for r in range(k):
                if dp[r]:
                    nr = (r * x) % k
                    curr[nr] += dp[r]

            dp = curr

            for r in range(k):
                ans[r] += dp[r]

        return ans