class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [0] * (1 << n)
        dp[0] = 1
        
        for mask in range(1 << n):
            pos = mask.bit_count() + 1
            
            for num in range(1, n + 1):
                if mask & (1 << (num - 1)):
                    continue
                
                if num % pos == 0 or pos % num == 0:
                    new_mask = mask | (1 << (num - 1))
                    dp[new_mask] += dp[mask]
        
        return dp[(1 << n) - 1]