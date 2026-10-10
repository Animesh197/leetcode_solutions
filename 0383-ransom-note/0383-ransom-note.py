class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        mp = Counter(magazine)

        for ch in ransomNote:
            if mp[ch] == 0:
                return False
            mp[ch] -= 1

        return True