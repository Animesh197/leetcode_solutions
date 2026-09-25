class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = [expression]
        res = set()
        
        while stack:
            curr = stack.pop()
            
            if '{' not in curr:
                res.add(curr)
                continue
                
            right = curr.find('}')
            left = curr.rfind('{', 0, right)
            
            before = curr[:left]
            after = curr[right+1:]
            
            middle = curr[left+1:right].split(',')
            
            for part in middle:
                stack.append(before + part + after)
                
        return sorted(list(res))