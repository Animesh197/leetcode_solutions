from collections import deque
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indeg = [0] * n
        vals = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1
            vals.add(w)

        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(vals)

        def check(limit):
            INF = 10**30
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and v != 0 and not online[v]:
                        continue

                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        lo, hi = 0, len(vals) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans