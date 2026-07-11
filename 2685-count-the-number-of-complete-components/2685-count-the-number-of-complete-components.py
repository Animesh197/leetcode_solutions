class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n
        count = 0

        def dfs(node, comp):
            vis[node] = True
            comp.append(node)

            for nei in adj[node]:
                if not vis[nei]:
                    dfs(nei, comp)

        for i in range(n):
            if not vis[i]:
                comp = []
                dfs(i, comp)

                size = len(comp)

                edgeCount = 0
                for node in comp:
                    edgeCount += len(adj[node])

                edgeCount //= 2  

                if edgeCount == size * (size - 1) // 2:
                    count += 1

        return count