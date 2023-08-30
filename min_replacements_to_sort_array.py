class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums),1):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    count+=1
        return count
            