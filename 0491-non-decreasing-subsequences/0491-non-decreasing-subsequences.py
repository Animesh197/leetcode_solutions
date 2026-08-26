class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []

        def solve(start):
            if len(curr) >= 2:
                ans.append(curr[:])

            used = set()

            for i in range(start, len(nums)):
                if curr and nums[i] < curr[-1]:
                    continue

                if nums[i] in used:
                    continue

                used.add(nums[i])
                curr.append(nums[i])

                solve(i + 1)

                curr.pop()

        solve(0)
        return ans