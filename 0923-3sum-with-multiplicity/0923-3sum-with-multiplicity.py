class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7

        count = [0] * 101

        for x in arr:
            count[x] += 1

        ans = 0

        for a in range(101):
            for b in range(a, 101):
                c = target - a - b

                if c < b or c > 100:
                    continue

                if a < b < c:
                    ways = count[a] * count[b] * count[c]

                elif a == b and b < c:
                    ways = (count[a] * (count[a] - 1) // 2) * count[c]

                elif a < b and b == c:
                    ways = count[a] * (count[b] * (count[b] - 1) // 2)

                else:
                    ways = count[a] * (count[a] - 1) * (count[a] - 2) // 6

                ans = (ans + ways) % MOD

        return ans