class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        tar = n//2
        ans = 0
        for i in range (n):
            ans += abs(nums[i] - nums[tar])
        return ans

        