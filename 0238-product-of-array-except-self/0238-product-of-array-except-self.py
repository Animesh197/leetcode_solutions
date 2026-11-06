class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        count = 0
        prod = 1
        for i in nums:
            if i ==0:
                count+=1
            if i != 0:
                prod *= i

        ans = [0]*n 
        if count >1:
            return ans 

        for i in range(n):
            if count == 1:
                if nums[i]==0:
                    ans[i] = prod
                
            else:
                ans[i] = int(prod/nums[i])

        return ans