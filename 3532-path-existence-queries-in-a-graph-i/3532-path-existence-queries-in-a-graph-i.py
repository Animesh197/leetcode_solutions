class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n

        c = 0
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                c += 1
            comp[i] = c

        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans