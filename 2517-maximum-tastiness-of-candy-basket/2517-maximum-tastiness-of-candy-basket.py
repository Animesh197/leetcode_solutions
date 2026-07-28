class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def possible(diff):
            count = 1
            last = price[0]

            for i in range(1, len(price)):
                if price[i] - last >= diff:
                    count += 1
                    last = price[i]
                    if count >= k:
                        return True

            return False

        left = 0
        right = price[-1] - price[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans