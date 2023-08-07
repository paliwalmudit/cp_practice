#brute (going down and right)
class Solution:
    def uniquePaths(self, m, n, i=0, j=0):
        if i >= m or j >= n:      return 0
        if i == m-1 and j == n-1: return 1
        return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)
#DFS
class Solution:
    def uniquePaths(self, m, n):
        def dfs(i, j):
            if i >= m or j >= n:      return 0
            if i == m-1 and j == n-1: return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0)