#binary search method, in CPP linear searth and sectionin method.
class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        print(l, r, mid)
        return l