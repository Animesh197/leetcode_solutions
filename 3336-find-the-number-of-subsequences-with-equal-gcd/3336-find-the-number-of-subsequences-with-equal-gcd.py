from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for x in nums:
            new_dp = defaultdict(int)

            for (g1, g2), cnt in dp.items():

                # Ignore x
                new_dp[(g1, g2)] = (new_dp[(g1, g2)] + cnt) % MOD

                # Put x in seq1
                ng1 = x if g1 == 0 else gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + cnt) % MOD

                # Put x in seq2
                ng2 = x if g2 == 0 else gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + cnt) % MOD

            dp = new_dp

        ans = 0
        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + cnt) % MOD

        return ans