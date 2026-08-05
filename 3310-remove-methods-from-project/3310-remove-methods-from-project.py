class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        
        for u, v in invocations:
            graph[u].append(v)
        
        suspicious = [False] * n
        
        def dfs(node):
            suspicious[node] = True
            
            for neigh in graph[node]:
                if not suspicious[neigh]:
                    dfs(neigh)
        
        dfs(k)
        
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        
        ans = []
        
        for node in range(n):
            if not suspicious[node]:
                ans.append(node)
        
        return ans