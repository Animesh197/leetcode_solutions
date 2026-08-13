class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [None] * (4 * n)
        ans = []

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left = a[0]
            right = b[1]

            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            # If the boundary characters are same,
            # we can join the suffix of left and prefix of right
            if a[1] == b[0]:
                best = max(best, a[3] + b[2])

                # Entire left segment has the same character
                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                # Entire right segment has the same character
                if b[3] == b[5]:
                    suffix = a[3] + b[5]

            length = a[5] + b[5]

            return (left, right, prefix, suffix, best, length)

        def build(node, start, end):
            if start == end:
                tree[node] = (s[start], s[start], 1, 1, 1, 1)
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        for i in range(len(queryCharacters)):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(tree[1][4])

        return ans