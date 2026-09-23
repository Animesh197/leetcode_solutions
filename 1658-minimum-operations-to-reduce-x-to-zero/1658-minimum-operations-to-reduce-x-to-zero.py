class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        rmd = total - x

        if rmd < 0:
            return -1

        l = 0
        current_sum = 0
        maxlen = -1

        for r in range(len(nums)):
            current_sum += nums[r]

            while current_sum > rmd and l <= r:
                current_sum -= nums[l]
                l += 1

            if current_sum == rmd:
                maxlen = max(maxlen, r - l + 1)

        if maxlen == -1:
            return -1

        return len(nums) - maxlen