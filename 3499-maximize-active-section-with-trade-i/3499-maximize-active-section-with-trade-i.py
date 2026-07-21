class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        arr = list(s)
        n = len(arr)
        count1 = 0

        block1 = 0
        block2 = 0
        maxx = 0

        i = 0
        while i < n:
            ch = arr[i]
            if ch == '0':
                block1 += 1
                i += 1
            else:
                while i < n and arr[i] == '1':
                    i += 1
                    count1 += 1

                while i < n and arr[i] == '0':
                    i += 1
                    block2 += 1

                if block1 != 0 and block2 != 0:
                    maxx = max(maxx, block1 + block2)
                block1 = block2
                block2 = 0

        return count1 + maxx