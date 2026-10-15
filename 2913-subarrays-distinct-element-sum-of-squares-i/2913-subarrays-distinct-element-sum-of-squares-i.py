class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            st = set()
            for j in range(i, n):
                st.add(nums[j])
                ans += len(st) ** 2

        return ans