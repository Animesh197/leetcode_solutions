class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            i = 0

            for ch in t:
                if i < len(s) and s[i] == ch:
                    i += 1

            return i == len(s)

        ans = -1

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i != j and isSubsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                ans = max(ans, len(strs[i]))

        return ans