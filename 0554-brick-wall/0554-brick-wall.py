class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = {}

        for row in wall:
            position = 0
            for i in range(len(row) - 1):
                position += row[i]
                if position in edges:
                    edges[position] += 1
                else:
                    edges[position] = 1

        maximum = 0

        for position in edges:
            if edges[position] > maximum:
                maximum = edges[position]

        return len(wall) - maximum