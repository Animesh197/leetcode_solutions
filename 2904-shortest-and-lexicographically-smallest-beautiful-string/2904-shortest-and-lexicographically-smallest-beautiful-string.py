class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        min_len = float('inf')
        answer = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            while ones == k:
                length = right - left + 1
                candidate = s[left:right + 1]

                if length < min_len:
                    min_len = length
                    answer = candidate
                elif length == min_len and candidate < answer:
                    answer = candidate

                if s[left] == '1':
                    ones -= 1
                left += 1

        return answer