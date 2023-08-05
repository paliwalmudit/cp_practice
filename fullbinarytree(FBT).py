class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1: return [TreeNode()]
        build = self.allPossibleFBT
        trees = []
        for i in range(1, n, 2):
            for l in build(n - i - 1):
                for r in build(i):
                    root = TreeNode(0, l, r)
                    trees.append(root)
        return trees