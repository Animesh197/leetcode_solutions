class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            idx = i % n

            while stack and stack[-1] <= nums[idx]:
                stack.pop()

            if stack:
                ans[idx] = stack[-1]

            stack.append(nums[idx])

        return ans