from bisect import bisect_left

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)
        
        pos = [[] for _ in range(26)]
        
        for i in range(n):
            pos[ord(word1[i]) - 97].append(i)
        
        exact = [-1] * (m + 1)
        one = [-1] * (m + 1)
        
        exact[m] = n
        one[m] = n
        
        for i in range(m - 1, -1, -1):
            c = ord(word2[i]) - 97
            
            p = bisect_left(pos[c], exact[i + 1]) - 1
            if p >= 0:
                exact[i] = pos[c][p]
            
            p = bisect_left(pos[c], one[i + 1]) - 1
            same = pos[c][p] if p >= 0 else -1
            
            limit = exact[i + 1] - 1
            
            if limit >= 0:
                if word1[limit] != word2[i]:
                    diff = limit
                else:
                    diff = limit - 1
            else:
                diff = -1
            
            one[i] = max(same, diff)
        
        ans = []
        index = -1
        used = False
        
        for i in range(m):
            found = False
            
            for j in range(index + 1, n):
                if word1[j] == word2[i]:
                    if one[i + 1] > j:
                        ans.append(j)
                        index = j
                        found = True
                        break
                elif not used:
                    if exact[i + 1] > j:
                        ans.append(j)
                        index = j
                        used = True
                        found = True
                        break
            
            if not found:
                return []
        
        return ans