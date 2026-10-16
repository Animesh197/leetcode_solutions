class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        sum_c = [0] * (4 * n + 4)
        sum_sq = [0] * (4 * n + 4)
        lazy = [0] * (4 * n + 4)
        
        def apply(node, L, R, val):
            length = R - L + 1
            sum_sq[node] = (sum_sq[node] + 2 * val * sum_c[node] + val * val * length) % MOD
            sum_c[node] = (sum_c[node] + val * length) % MOD
            lazy[node] += val
            
        def push_down(node, L, R):
            if lazy[node]:
                mid = (L + R) // 2
                apply(2 * node, L, mid, lazy[node])
                apply(2 * node + 1, mid + 1, R, lazy[node])
                lazy[node] = 0
                
        def push_up(node):
            sum_c[node] = (sum_c[2 * node] + sum_c[2 * node + 1]) % MOD
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            
        def update(node, L, R, ql, qr, val):
            if ql <= L and R <= qr:
                apply(node, L, R, val)
                return
            push_down(node, L, R)
            mid = (L + R) // 2
            if ql <= mid:
                update(2 * node, L, mid, ql, qr, val)
            if qr > mid:
                update(2 * node + 1, mid + 1, R, ql, qr, val)
            push_up(node)
            
        last = {}
        ans = 0
        
        for i, x in enumerate(nums, 1):
            p = last.get(x, 0)
            update(1, 1, n, p + 1, i, 1)
            ans = (ans + sum_sq[1]) % MOD
            last[x] = i
            
        return ans