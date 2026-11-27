class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = 1500
        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1
        
        div_count = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            for mult in range(f, max_f + 1, f):
                div_count[f] += freq[mult]
                
        dp = [0] * (budget + 1)
        min_price = min(p for _, p in items)
        
        for f, p in items:
            first_val = div_count[f]
            for b in range(budget, p - 1, -1):
                if dp[b - p] + first_val > dp[b]:
                    dp[b] = dp[b - p] + first_val
                    
        for b in range(min_price, budget + 1):
            if dp[b - min_price] + 1 > dp[b]:
                dp[b] = dp[b - min_price] + 1
                
        return max(dp)