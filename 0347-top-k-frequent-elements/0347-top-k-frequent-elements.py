from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in freq:
            count = freq[num]
            buckets[count].append(num)

        ans = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                ans.append(num)

                if len(ans) == k:
                    return ans