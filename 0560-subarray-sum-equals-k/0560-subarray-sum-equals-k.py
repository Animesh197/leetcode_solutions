class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        curr = 0
        ans = 0

        for num in nums:
            curr += num

            if curr - k in mp:
                ans += mp[curr - k]

            if curr in mp:
                mp[curr] += 1
            else:
                mp[curr] = 1

        return ans