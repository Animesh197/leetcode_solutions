class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        elif len(nums)==2:
            return 2
        mini = 10**6
        maxi = -10**(6)
        mini_idx = 0 
        maxi_idx = 0 

        for i in range (len(nums)):
            if nums[i]<mini:
                mini = nums[i]
                mini_idx = i

        for i in range (len(nums)):
            if nums[i]>maxi:
                maxi = nums[i]
                maxi_idx = i
        # print(len(nums), mini_idx, maxi_idx)
        # print(mini, maxi)
        f = max(mini_idx, maxi_idx)+1
        b = len(nums) - min(maxi_idx,mini_idx)
        both = min(maxi_idx,mini_idx)+1 + len(nums) - max(maxi_idx,mini_idx)
        
        return min(f,b,both)