class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                v = stack.pop()
                if v == 0:
                    score = 1
                else:
                    score = 2*v
                stack[-1] += score

        return stack[0]


        