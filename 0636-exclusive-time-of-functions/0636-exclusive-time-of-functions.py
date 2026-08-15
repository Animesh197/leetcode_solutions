class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev = 0
        
        for log in logs:
            parts = log.split(":")
            func = int(parts[0])
            typ = parts[1]
            time = int(parts[2])
            
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev
                
                stack.append(func)
                prev = time
            
            else:
                ans[stack.pop()] += time - prev + 1
                prev = time + 1
        
        return ans