class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return True
        arr=sorted(arr)
        d=arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i] != arr[0] + i * d:
                return False
        return True