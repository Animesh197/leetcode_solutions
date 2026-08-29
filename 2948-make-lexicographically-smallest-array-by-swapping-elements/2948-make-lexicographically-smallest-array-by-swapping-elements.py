class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        a = []

        for i in range(n):
            a.append((nums[i], i))

        a.sort()
        ans = nums[:]
        i = 0

        while i < n:
            j = i
            while j + 1 < n:
                if a[j + 1][0] - a[j][0] <= limit:
                    j += 1
                else:
                    break
            v = []
            p = []

            for k in range(i, j + 1):
                v.append(a[k][0])
                p.append(a[k][1])

            p.sort()

            for k in range(len(v)):
                ans[p[k]] = v[k]

            i = j + 1

        return ans