class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))

        rank = {}
        r = 1

        for x in nums:
            rank[x] = r
            r += 1

        ans = []

        for x in arr:
            ans.append(rank[x])

        return ans