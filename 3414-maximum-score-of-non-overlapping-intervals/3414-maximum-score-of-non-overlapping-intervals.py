from bisect import bisect_left
class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        a = []

        for i in range(n):
            l = intervals[i][0]
            r = intervals[i][1]
            w = intervals[i][2]
            a.append((l, r, w, i))

        a.sort(key=lambda x: x[1])
        ends = []

        for x in a:
            ends.append(x[1])

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):
                l = a[i - 1][0]
                w = a[i - 1][2]
                index = a[i - 1][3]

                best = dp[k][i - 1]

                p = bisect_left(ends, l, 0, i - 1)

                old_score = dp[k - 1][p][0]
                old_indices = dp[k - 1][p][1]

                new_score = old_score + w
                new_indices = tuple(sorted(old_indices + (index,)))

                if new_score > best[0]:
                    best = (new_score, new_indices)
                elif new_score == best[0] and new_indices < best[1]:
                    best = (new_score, new_indices)

                dp[k][i] = best

        return list(dp[4][n][1])