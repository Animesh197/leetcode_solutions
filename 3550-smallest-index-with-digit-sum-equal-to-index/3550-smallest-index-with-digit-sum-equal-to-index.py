class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            sm = 0

            while x:
                sm += x % 10
                x //= 10

            if sm == i:
                return i

        return -1