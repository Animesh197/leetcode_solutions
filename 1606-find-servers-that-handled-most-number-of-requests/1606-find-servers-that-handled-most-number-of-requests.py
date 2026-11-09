import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(i, val):
            i += size
            tree[i] = val
            i //= 2

            while i:
                tree[i] = tree[2 * i] + tree[2 * i + 1]
                i //= 2

        def find(node, l, r, start):
            if r <= start or tree[node] == 0:
                return -1

            if l == r - 1:
                return l

            mid = (l + r) // 2

            ans = find(2 * node, l, mid, start)

            if ans != -1:
                return ans

            return find(2 * node + 1, mid, r, start)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)

            if tree[1] == 0:
                continue

            start = i % k
            server = find(1, 0, size, start)

            if server == -1:
                server = find(1, 0, size, 0)

            update(server, 0)
            count[server] += 1

            heapq.heappush(busy, (arrival[i] + load[i], server))

        mx = max(count)
        return [i for i in range(k) if count[i] == mx]