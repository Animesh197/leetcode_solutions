class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}
        
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        def solve(i, m):
            if i >= n:
                return 0
            
            if (i, m) in dp:
                return dp[(i, m)]
            
            ans = 0
            
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                
                remaining = suffix[i + x]
                curr = suffix[i] - remaining
                
                next_m = max(m, x)
                curr += remaining - solve(i + x, next_m)
                
                ans = max(ans, curr)
            
            dp[(i, m)] = ans
            return ans
        
        return solve(0, 1)