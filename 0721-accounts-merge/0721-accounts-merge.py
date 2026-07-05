class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa

        mp = {}

        # Merge accounts have common email
        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in mp:
                    union(i, mp[email])
                else:
                    mp[email] = i

        grp = {}

        # Group emails by parent
        for email, idx in mp.items():
            p = find(idx)
            if p not in grp:
                grp[p] = []
            grp[p].append(email)

        ans = []

        for p in grp:
            ans.append([accounts[p][0]] + sorted(grp[p]))

        return ans