class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        curr = n
        while curr > 0:
            count+=1
            curr = curr//10
        # return count

        if count <= 3:
            return 0

        k = (count-1)//3
        return n - (10**(k*3)) + 1
        # print(k)


        