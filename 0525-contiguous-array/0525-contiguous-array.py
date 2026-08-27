class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        prefix = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in first:
                ans = max(ans, i - first[prefix])
            else:
                first[prefix] = i

        return ans