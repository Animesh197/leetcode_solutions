class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            ghost_dist = abs(x - target[0]) + abs(y - target[1])

            if ghost_dist <= my_dist:
                return False

        return True