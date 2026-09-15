from bisect import bisect_right

class Solution:
    def makeArrayIncreasing(self, arr1, arr2):
        arr2 = sorted(set(arr2))

        dp = {-1: 0}

        for x in arr1:
            new_dp = {}

            for prev in dp:
                operations = dp[prev]

                if x > prev:
                    if x not in new_dp or operations < new_dp[x]:
                        new_dp[x] = operations

                index = bisect_right(arr2, prev)

                if index < len(arr2):
                    value = arr2[index]
                    new_operations = operations + 1

                    if value not in new_dp or new_operations < new_dp[value]:
                        new_dp[value] = new_operations

            dp = new_dp

            if not dp:
                return -1

        answer = float('inf')

        for value in dp:
            answer = min(answer, dp[value])

        if answer == float('inf'):
            return -1

        return answer