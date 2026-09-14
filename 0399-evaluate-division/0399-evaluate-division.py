class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u,v),val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0/val

        def dfs(cur,target,visited):
            if cur not in graph or target not in graph:
                return -1.0
            if cur == target:
                return 1.0

            visited.add(cur)
            for nei , wt in graph[cur].items():
                if nei not in visited:
                    result = dfs(nei,target,visited)
                    if result != -1.0:
                        return wt*result
            return -1.0

        results = []
        for start,end in queries:
            results.append(dfs(start,end,set()))

        return results