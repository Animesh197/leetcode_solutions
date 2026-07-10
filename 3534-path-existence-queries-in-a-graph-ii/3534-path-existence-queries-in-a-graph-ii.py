from bisect import bisect_right
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))

        val = [x[0] for x in arr]
        idx = [x[1] for x in arr]

        pos = [0] * n
        for i in range(n):
            pos[idx[i]] = i

        comp = [0] * n
        c = 0
        for i in range(1, n):
            if val[i] - val[i - 1] > maxDiff:
                c += 1
            comp[i] = c

        compNode = [0] * n
        for i in range(n):
            compNode[idx[i]] = comp[i]

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and val[j + 1] - val[i] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = 18
        up = [[0] * n for _ in range(LOG)]
        up[0] = nxt[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            if compNode[u] != compNode[v]:
                ans.append(-1)
                continue

            a = pos[u]
            b = pos[v]

            if a > b:
                a, b = b, a

            cur = a
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    dist += 1 << k

            ans.append(dist + 1)

        return ans