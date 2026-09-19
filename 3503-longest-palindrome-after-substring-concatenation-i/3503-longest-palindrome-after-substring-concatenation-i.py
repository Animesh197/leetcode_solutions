class Solution:
    def longestPalindrome(self, s, t):
        n = len(s)
        m = len(t)
        ans = 1

        for i in range(n + 1):
            for j in range(i, n + 1):
                a = s[i:j]

                for x in range(m + 1):
                    for y in range(x, m + 1):
                        b = t[x:y]
                        curr = a + b

                        if curr == curr[::-1]:
                            ans = max(ans, len(curr))

        return ans