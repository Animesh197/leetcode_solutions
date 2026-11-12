class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cur = 1
        maxi = 1

        for i in range(1,n):
            if nums[i]>nums[i-1]:
                cur+=1
            else:
                cur = 1
            maxi = max(cur,maxi)


        cur = 1
        # maxi = 1

        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                cur+=1
            else:
                cur = 1
            maxi = max(cur,maxi)

        return maxi
