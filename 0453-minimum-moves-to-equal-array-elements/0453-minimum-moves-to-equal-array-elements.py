from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        ans = 0

        for x in nums:
            ans += x - mn

        return ans