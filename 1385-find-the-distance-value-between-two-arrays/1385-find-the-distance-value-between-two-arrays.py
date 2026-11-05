class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """

        i,j = 0,0
        ans = 0

        while i < len(arr1):
            if abs(arr1[i]- arr2[j]) <= d:
                i+=1
                j=0
                continue
            j+=1
            if j == len(arr2):
                ans+=1
                j=0
                i+=1
        return (ans)