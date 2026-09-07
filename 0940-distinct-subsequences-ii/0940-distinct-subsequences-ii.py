class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        last = [-1] * 26
        
        dp[0] = 1
        
        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]
            index = ord(s[i - 1]) - ord('a')
            
            if last[index] != -1:
                dp[i] -= dp[last[index]]
            
            dp[i] %= MOD
            last[index] = i - 1
            
        return (dp[n] - 1) % MOD