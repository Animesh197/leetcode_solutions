class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)

        dp=[[-1]*(m+1) for _ in range(n+1)]

        def solve(i,j):
            if j>=m:
                return 1
            if i>=n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            pick=0
            if s[i]==t[j]:
                pick=solve(i+1,j+1)
            notpick= solve(i+1,j)

            dp[i][j]=pick+notpick
            return dp[i][j]

        return (solve(0,0))
                
                