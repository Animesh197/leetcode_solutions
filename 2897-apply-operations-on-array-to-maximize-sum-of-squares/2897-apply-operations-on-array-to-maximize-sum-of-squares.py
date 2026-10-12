class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 32

        for x in nums:
            for i in range(32):
                if x & (1 << i):
                    cnt[i] += 1

        ans = 0

        for _ in range(k):
            curr = 0
            for i in range(32):
                if cnt[i] > 0:
                    curr |= 1 << i
                    cnt[i] -= 1
            ans = (ans + curr * curr) % mod

        return ans