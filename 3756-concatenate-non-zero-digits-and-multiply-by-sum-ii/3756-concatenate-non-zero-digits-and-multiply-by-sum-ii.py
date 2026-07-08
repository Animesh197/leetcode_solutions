class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Store non-zero digits and their positions
        digits = []
        pos = []
        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        # Prefix sum of digits
        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digits[i]

        # Prefix value of concatenated number
        prefVal = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        for i in range(m):
            pow10[i + 1] = (pow10[i] * 10) % MOD
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD

        from bisect import bisect_left, bisect_right

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (prefVal[right + 1] - prefVal[left] * pow10[length]) % MOD
            digit_sum = prefSum[right + 1] - prefSum[left]

            ans.append((x * digit_sum) % MOD)

        return ans