class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1

            elif num == cand2:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1

            elif count2 == 0:
                cand2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Verify candidates
        count1 = count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        result = []
        n = len(nums)

        if count1 > n // 3:
            result.append(cand1)

        if count2 > n // 3:
            result.append(cand2)

        return result