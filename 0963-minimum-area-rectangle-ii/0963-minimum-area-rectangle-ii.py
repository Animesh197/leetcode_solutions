import collections
import math

class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        n = len(points)
        mp = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                mid = (x1 + x2, y1 + y2)
                dist_sq = (x1 - x2)**2 + (y1 - y2)**2
                
                mp[(mid, dist_sq)].append((points[i], points[j]))
                
        ans = float('inf')
        
        for pairs in mp.values():
            if len(pairs) > 1:
                for i in range(len(pairs)):
                    for j in range(i + 1, len(pairs)):
                        p1, p2 = pairs[i]
                        p3, p4 = pairs[j]
                        
                        side1_sq = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
                        side2_sq = (p1[0] - p4[0])**2 + (p1[1] - p4[1])**2
                        
                        area = math.sqrt(side1_sq * side2_sq)
                        ans = min(ans, area)
                        
        return ans if ans != float('inf') else 0.0