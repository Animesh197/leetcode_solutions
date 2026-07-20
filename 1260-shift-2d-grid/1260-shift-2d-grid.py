class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        total = rows * cols
        k = k % total

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                old_index = i * cols + j
                new_index = (old_index + k) % total

                new_row = new_index // cols
                new_col = new_index % cols

                ans[new_row][new_col] = grid[i][j]

        return ans