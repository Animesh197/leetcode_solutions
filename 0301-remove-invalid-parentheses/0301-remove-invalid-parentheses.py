class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        remove_open = 0
        remove_close = 0

        for ch in s:
            if ch == "(":
                remove_open += 1
            elif ch == ")":
                if remove_open > 0:
                    remove_open -= 1
                else:
                    remove_close += 1

        ans = set()

        def solve(i, curr, balance, ro, rc):
            if i == len(s):
                if balance == 0 and rc == 0 and ro == 0:
                    ans.add(curr)
                return 

            ch = s[i]
            if ch == "(":
                if ro > 0:
                    solve(i+1, curr, balance, ro-1, rc)
                solve(i+1, curr + ch, balance+1, ro, rc)
            
            elif ch == ")":
                if rc>0:
                    solve(i+1, curr, balance, ro, rc-1)
                if balance >0:
                    solve(i+1, curr + ch, balance-1, ro, rc)

            else:
                solve(i+1, curr + ch, balance, ro, rc)

        solve(0, "", 0, remove_open, remove_close)

        return list(ans)

            