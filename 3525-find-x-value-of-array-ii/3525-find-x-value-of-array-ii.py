from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        prod = [1] * (4 * n)
        pref = [[0] * k for _ in range(4 * n)]
        
        def build(node: int, start: int, end: int):
            if start == end:
                v = nums[start] % k
                prod[node] = v
                pref[node][v] = 1
                return
            
            mid = (start + end) // 2
            left = 2 * node
            right = 2 * node + 1
            
            build(left, start, mid)
            build(right, mid + 1, end)
            
            prod[node] = (prod[left] * prod[right]) % k
            for i in range(k):
                pref[node][i] = pref[left][i]
            
            lp = prod[left]
            for r in range(k):
                if pref[right][r] > 0:
                    nv = (lp * r) % k
                    pref[node][nv] += pref[right][r]
                    
        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                v = val % k
                prod[node] = v
                for i in range(k):
                    pref[node][i] = 0
                pref[node][v] = 1
                return
            
            mid = (start + end) // 2
            left = 2 * node
            right = 2 * node + 1
            
            if start <= idx <= mid:
                update(left, start, mid, idx, val)
            else:
                update(right, mid + 1, end, idx, val)
                
            prod[node] = (prod[left] * prod[right]) % k
            for i in range(k):
                pref[node][i] = pref[left][i]
            
            lp = prod[left]
            for r in range(k):
                if pref[right][r] > 0:
                    nv = (lp * r) % k
                    pref[node][nv] += pref[right][r]

        def query(node: int, start: int, end: int, l: int, r: int):
            if l <= start and end <= r:
                return prod[node], pref[node]
            
            mid = (start + end) // 2
            if r <= mid:
                return query(2 * node, start, mid, l, r)
            elif l > mid:
                return query(2 * node + 1, mid + 1, end, l, r)
            
            left_prod, left_pref = query(2 * node, start, mid, l, r)
            right_prod, right_pref = query(2 * node + 1, mid + 1, end, l, r)
            
            res_prod = (left_prod * right_prod) % k
            res_pref = left_pref[:]
            
            for i in range(k):
                if right_pref[i] > 0:
                    nv = (left_prod * i) % k
                    res_pref[nv] += right_pref[i]
                    
            return res_prod, res_pref

        build(1, 0, n - 1)
        
        ans = []
        for idx, val, start_i, x_i in queries:
            update(1, 0, n - 1, idx, val)
            _, p_counts = query(1, 0, n - 1, start_i, n - 1)
            ans.append(p_counts[x_i])
            
        return ans