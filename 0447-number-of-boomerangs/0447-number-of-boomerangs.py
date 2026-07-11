from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0
        n = len(points)

        for i in range(n):
            mp = defaultdict(int)

            x1, y1 = points[i]

            for j in range(n):
                if i == j:
                    continue

                x2, y2 = points[j]

                dx = x1 - x2
                dy = y1 - y2

                dist = dx * dx + dy * dy
                mp[dist] += 1

            for cnt in mp.values():
                ans += cnt * (cnt - 1)

        return ans