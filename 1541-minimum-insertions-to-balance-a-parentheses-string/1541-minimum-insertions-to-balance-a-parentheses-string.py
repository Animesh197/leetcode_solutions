class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        n = len(s)
        ans = 0

        i = 0
        while i<n:
            if s[i]=="(":
                count+=1
                i+=1

            else:
                if count<=0:
                    if i+1<n and s[i] == ")" and s[i+1] ==")":
                        ans+=1
                        i+=2
                    elif s[i] == ")":
                        ans+=2
                        i+=1
                else:
                    
                    if i+1< n and s[i] == ")" and s[i+1] ==")" :
                        count-=1
                        i+=2
                    elif s[i] == ")":
                        count -=1 
                        i+=1
                        ans+=1

        return ans + 2*count
                    
                    