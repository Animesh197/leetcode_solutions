class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        cur = 0
        maxi = sum(nums)

        for i in range (n):
            if cur == maxi-cur-nums[i]:
                return i

            cur+=nums[i]
        return -1
        