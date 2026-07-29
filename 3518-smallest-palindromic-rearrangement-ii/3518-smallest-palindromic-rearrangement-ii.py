class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1:
            return s if k == 1 else ""
        mid = s[n // 2] if n % 2 == 1 else ""
        n //= 2
        freq = Counter(s[:n])
        hs = []
        for c in ascii_lowercase:
            hs += [c] * freq[c]
        l, con, pm = 0, 0, 1
        prev = "A"
        freq = {}
        for c in hs[::-1]:
            l += 1
            con = con + 1 if c == prev else 1
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            pm = pm * l // con
            prev = c
            if pm >= k:
                ss = sorted(freq.keys())
                while l > 0:
                    for c in ss:
                        if freq[c] == 0:
                            continue
                        p = pm * freq[c] // l
                        if k <= p:
                            hs[n - l] = c
                            pm = p
                            freq[c] -= 1
                            break
                        k -= p
                    l -= 1
                return "".join(hs + [mid] + hs[::-1])
        return ""