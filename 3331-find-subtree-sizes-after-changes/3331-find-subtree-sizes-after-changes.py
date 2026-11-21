
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        new_tree = [[] for _ in range(n)]
        par = parent[:]

        last = {}
        order = []

        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()

            if state == 1:
                last[s[node]] = prev
                continue

            old = last.get(s[node], -1)

            if old != -1:
                par[node] = old

            new_tree[par[node]].append(node)

            last[s[node]] = node
            order.append(node)

            stack.append((node, 1, old))

            for child in reversed(tree[node]):
                stack.append((child, 0, -1))

        ans = [1] * n

        for node in reversed(order):
            if node != 0:
                ans[par[node]] += ans[node]

        return ans
