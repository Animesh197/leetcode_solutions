class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')

            return name[0] + '*****' + name[-1] + '@' + domain

        digits = ""

        for ch in s:
            if ch.isdigit():
                digits += ch

        country = len(digits) - 10
        last4 = digits[-4:]

        if country == 0:
            return "***-***-" + last4

        return "+" + "*" * country + "-***-***-" + last4