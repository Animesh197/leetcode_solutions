class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        values = set(nums)
        start = min(nums)
        end = max(nums)
        
        ans = []
        for num in range(start, end + 1):
            
            if num not in values:
                ans.append(num)
        
        return ans