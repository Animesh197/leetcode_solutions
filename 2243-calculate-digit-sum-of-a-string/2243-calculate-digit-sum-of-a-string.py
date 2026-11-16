class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # n = len(s)
        

        while len(s)>k:
            m = ""

            for i in range(0,len(s),k):
                cur = s[i:i+k]
                
                agg = 0
                for dig in cur:
                    agg+=int(dig)

                m = m + str(agg)
            s = m

        return s

            

        