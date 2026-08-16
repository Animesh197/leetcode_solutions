class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]
        for x in stones:
            cnt[x % 3] += 1

        c0, c1, c2 = cnt

        if c1 == 0 or c2 == 0:
            return max(c1, c2) > 2 and c0 % 2 == 1

        return abs(c1 - c2) > 2 or c0 % 2 == 0