class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        
        even = 1
        odd = 0
        curr = 0
        res = 0
        
        for x in arr:
            curr += x
            
            if curr % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
        
        return res % mod