class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cur_max = -float("inf")
        cur_min = float("inf")
        mini = ['a']*n
        maxi = ['b']*n
        for i in range (n):
            if cur_max <= nums[i]:
                cur_max = nums[i]
                maxi[i] = nums[i]
            else:
                maxi[i] = cur_max
        
        for i in range (n-1,-1,-1):
            if cur_min > nums[i]:
                cur_min = nums[i]
                mini[i] = nums[i]
            else:
                mini[i] = cur_min

        # print(maxi)
        # print(mini)

        for i in range (n):
            if maxi[i] - mini[i] <= k:
                return i

        else:
            return -1
        