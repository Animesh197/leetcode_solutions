class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        open = 0

        for ch in s:
            if ch == '[':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    open += 1

        return (open + 1) // 2