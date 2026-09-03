class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()

        order = []
        for i in range(n):
            order.append((nums2[i], i))
        
        order.sort(reverse=True)

        ans = [0] * n

        left = 0
        right = n - 1

        for i in range(n):
            value = order[i][0]
            index = order[i][1]

            if nums1[right] > value:
                ans[index] = nums1[right]
                right -= 1
            else:
                ans[index] = nums1[left]
                left += 1

        return ans