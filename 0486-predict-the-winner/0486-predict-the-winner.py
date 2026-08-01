from functools import lru_cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(l, r):
            if l == r:
                return nums[l]

            take_left = nums[l] - dp(l + 1, r)
            take_right = nums[r] - dp(l, r - 1)

            return max(take_left, take_right)

        return dp(0, len(nums) - 1) >= 0