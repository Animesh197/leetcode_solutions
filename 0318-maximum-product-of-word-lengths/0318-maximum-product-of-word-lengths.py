class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        for i in range(n):
            mask = 0
            for ch in words[i]:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask
            lengths[i] = len(words[i])

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, lengths[i] * lengths[j])

        return ans