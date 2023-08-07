class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            for j in i:
                if j==target:
                    return True

        return False
# can also be solved by binary search and 2 pointer matrix traversal.