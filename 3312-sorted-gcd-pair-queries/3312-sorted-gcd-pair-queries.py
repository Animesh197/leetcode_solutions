from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for j in range(d, mx + 1, d):
                cnt[d] += freq[j]

        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            c = cnt[d]
            pairs = c * (c - 1) // 2

            m = 2 * d
            while m <= mx:
                pairs -= exact[m]
                m += d

            exact[d] = pairs

        values = []
        prefix = []

        total = 0
        for d in range(1, mx + 1):
            if exact[d] > 0:
                total += exact[d]
                values.append(d)
                prefix.append(total)

        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans