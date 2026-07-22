class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            ans = 1

            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(ni, nj))

            dp[i][j] = ans
            return ans

        res = 0

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res