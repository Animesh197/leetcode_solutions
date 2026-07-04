from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        ans = float('inf')

        q = deque([1])
        visited.add(1)

        while q:
            u = q.popleft()

            for v, w in graph[u]:
                ans = min(ans, w)
                if v not in visited:
                    visited.add(v)
                    q.append(v)

        return ans