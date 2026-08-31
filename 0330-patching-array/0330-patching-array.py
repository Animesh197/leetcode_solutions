class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sum1 = 0
        patch_count = 0
        i = 0

        while sum1 < n:
            if i >= len(nums) or nums[i] > sum1 + 1:
                patch_count += 1
                sum1 += sum1 + 1
            else:
                sum1 += nums[i]
                i += 1
                
        return patch_count