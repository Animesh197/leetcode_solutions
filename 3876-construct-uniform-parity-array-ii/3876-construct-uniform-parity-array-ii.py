class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        if min_val & 1:
            return True
            
        for x in nums1:
            if x & 1:
                return False
                
        return True