class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        count = 0
        for char in s:
            if char == "(":
                count+=1

            if count >1:
                ans+=char
            if char == ")":
                count -=1

            

        return ans
        