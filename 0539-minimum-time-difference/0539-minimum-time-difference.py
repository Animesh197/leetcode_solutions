class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            nums.append(h * 60 + m)

        nums.sort()

        ans = 1440

        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])

        ans = min(ans, nums[0] + 1440 - nums[-1])

        return ans