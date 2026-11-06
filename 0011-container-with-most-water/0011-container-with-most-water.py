class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)

        i,j = 0,n-1
        capacity = 0

        while i<j:   

            if height[i]<height[j]:
                cur_cap = (height[i])*(j-i)
                i+=1
            else:
                cur_cap = (height[j])*(j-i)
                j-=1
            capacity = max(capacity, cur_cap)

        return capacity

        