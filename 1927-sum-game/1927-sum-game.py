class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        diff = 0
        q = 0
        
        for i in range(half):
            if num[i] == '?':
                q += 1
            else:
                diff += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                q -= 1
            else:
                diff -= int(num[i])
                
        # If the total number of '?' is odd, Alice always wins.
        if q % 2 != 0:
            return True
            
        # Bob wins ONLY if he can exactly balance the difference.
        return diff + (q // 2) * 9 != 0