class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0

        for char in s:
            if char == "(":
                stack.append("(")
            else:
                if not stack:
                    ans+=1
                else:
                    stack.pop()

        return len(stack) + ans


        