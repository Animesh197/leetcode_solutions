class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXX = 2048

        present = [0] * MAXX
        for x in nums:
            present[x] = 1

        one = present[:]

        two = [0] * MAXX
        vals = [i for i in range(MAXX) if one[i]]

        for a in vals:
            for b in vals:
                two[a ^ b] = 1

        ans = [0] * MAXX
        vals2 = [i for i in range(MAXX) if two[i]]

        for x in vals2:
            for y in vals:
                ans[x ^ y] = 1

        return sum(ans)