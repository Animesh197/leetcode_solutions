from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        d = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    d[i][j] = 0
                    q.append((i, j))

        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

        pq = [(-d[0][0], 0, 0)]
        vis = [[0] * n for _ in range(n)]

        while pq:
            val, x, y = heapq.heappop(pq)
            val = -val

            if vis[x][y]:
                continue
            vis[x][y] = 1

            if x == n - 1 and y == n - 1:
                return val

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
                    heapq.heappush(pq, (-min(val, d[nx][ny]), nx, ny))

        return 0