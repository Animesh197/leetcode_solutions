class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        st = set(wordDict)
        memo = {}

        def solve(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]

            ans = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word not in st:
                    continue
                for x in solve(j):
                    if x:
                        ans.append(word + " " + x)
                    else:
                        ans.append(word)

            memo[i] = ans
            return ans

        return solve(0)