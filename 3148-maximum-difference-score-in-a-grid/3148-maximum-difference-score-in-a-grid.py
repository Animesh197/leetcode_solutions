class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_score = float('-inf')
        
        for i in range(m):
            for j in range(n):
                prev_min = float('inf')
                
                if i > 0:
                    prev_min = min(prev_min, grid[i-1][j])
                if j > 0:
                    prev_min = min(prev_min, grid[i][j-1])
                
                if prev_min != float('inf'):
                    max_score = max(max_score, grid[i][j] - prev_min)
                    grid[i][j] = min(grid[i][j], prev_min)
                    
        return max_score