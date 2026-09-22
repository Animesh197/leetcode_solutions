class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k<2:
            return k
        fib = [1,1]
        while fib[-1]<k:
            fib.append(fib[-1]+fib[-2])
        i=len(fib)-1
        count=0
        while k>0:
            if fib[i]<=k:
                k-=fib[i]
                count+=1
            else:
                i-=1
        return count