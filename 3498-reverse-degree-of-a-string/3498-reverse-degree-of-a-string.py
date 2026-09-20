class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            val = ord(s[i]) - ord('a')
            rev = 26 - val
            ans += rev * (i + 1)

        return ans