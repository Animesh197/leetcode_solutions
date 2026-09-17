from collections import deque

class Solution:
    def colorGrid(self, n, m, sources):
        mat = [[0]*m for _ in range(n)]
        time = [[float('inf')]*m for _ in range(n)]

        q = deque()

        for r, c, color in sources:
            mat[r][c] = color
            time[r][c] = 0
            q.append((r, c, color))

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        while q:
            x, y, c = q.popleft()
            dist = time[x][y] + 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:

                    if time[nx][ny] == dist:
                        if mat[nx][ny] < c:
                            mat[nx][ny] = c
                            q.append((nx, ny, c))

                    elif time[nx][ny] > dist:
                        time[nx][ny] = dist
                        mat[nx][ny] = c
                        q.append((nx, ny, c))

        return mat