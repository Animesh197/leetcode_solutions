class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
            
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                if i > 0:
                    for v in dp[i - 1][j]:
                        nv = v + 1 if grid[i][j] == '(' else v - 1
                        if nv >= 0:
                            dp[i][j].add(nv)
                            
                if j > 0:
                    for v in dp[i][j - 1]:
                        nv = v + 1 if grid[i][j] == '(' else v - 1
                        if nv >= 0:
                            dp[i][j].add(nv)

        return 0 in dp[-1][-1]