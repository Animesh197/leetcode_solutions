class Solution:
    def findKthSmallest(self, coins, k):
        from math import gcd

        n = len(coins)
        coins.sort()

        useful = []

        for c in coins:
            if all(c % x != 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        # Count how many valid amounts are <= x
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        # Binary search
        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low