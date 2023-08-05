from collections import Counter as cs
class Solution(object):
    def majorityElement(self, nums):
        return cs.most_common(cs(nums))[0][0]
        