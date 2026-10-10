class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        l = 0
        r = max(diff)

        while l < r:
            mid = (l + r) // 2
            curr = sum(max(0, x - mid) for x in diff)

            if curr <= k:
                r = mid
            else:
                l = mid + 1

        ans = 0
        used = 0

        for x in diff:
            if x > l:
                ans += l * l
                used += x - l
            else:
                ans += x * x

        rem = k - used
        return ans - rem * (2 * l - 1)