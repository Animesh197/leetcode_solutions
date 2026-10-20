class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        ans = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            possible = True
            for i in range(0, n, k):
                block = nums[i:i + k]
                block_s = s[i:i + k]
                
                drops = 0
                drop_idx = -1
                
                for j in range(k - 1):
                    if block[j] > block[j + 1]:
                        drops += 1
                        drop_idx = j
                        
                if block[-1] > block[0]:
                    drops += 1
                    drop_idx = k - 1
                    
                if drops > 1:
                    possible = False
                    break
                    
                if drops == 0:
                    if block != block_s:
                        possible = False
                        break
                elif drops == 1:
                    shifted = block[drop_idx + 1:] + block[:drop_idx + 1]
                    if shifted != block_s:
                        possible = False
                        break
                        
            if possible:
                ans += k
                
        return ans