class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - 97] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if count[x] == 0:
                break

            ans.append(target[i])
            count[x] -= 1
        else:
            for i in range(len(target) - 1, -1, -1):
                x = ord(target[i]) - 97
                count[x] += 1
                ans.pop()

                for bigger in range(x + 1, 26):
                    if count[bigger] > 0:
                        res = ans + [chr(bigger + 97)]
                        count[bigger] -= 1

                        for j in range(26):
                            res += [chr(j + 97)] * count[j]

                        return ''.join(res)

            return ""

        i = len(ans)
        x = ord(target[i]) - 97

        for bigger in range(x + 1, 26):
            if count[bigger] > 0:
                ans.append(chr(bigger + 97))
                count[bigger] -= 1

                for j in range(26):
                    ans += [chr(j + 97)] * count[j]

                return ''.join(ans)

        for i in range(len(ans) - 1, -1, -1):
            x = ord(ans[i]) - 97
            count[x] += 1
            ans.pop()

            for bigger in range(x + 1, 26):
                if count[bigger] > 0:
                    res = ans + [chr(bigger + 97)]
                    count[bigger] -= 1

                    for j in range(26):
                        res += [chr(j + 97)] * count[j]

                    return ''.join(res)

        return ""