class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        ans = []

        while len(s) > k:
            ans.append(s[-k:])
            s = s[:-k]

        ans.append(s)

        return "-".join(ans[::-1])