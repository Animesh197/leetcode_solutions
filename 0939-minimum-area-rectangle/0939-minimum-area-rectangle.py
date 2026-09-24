class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        st = set((x, y) for x, y in points)
        ans = float('inf')

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in st and (x2, y1) in st:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    ans = min(ans, area)

        return 0 if ans == float('inf') else ans