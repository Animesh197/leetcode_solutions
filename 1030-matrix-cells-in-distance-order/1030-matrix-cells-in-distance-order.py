class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        ans = []

        for i in range(rows):
            for j in range(cols):
                ans.append([i, j])

        ans.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))

        return ans