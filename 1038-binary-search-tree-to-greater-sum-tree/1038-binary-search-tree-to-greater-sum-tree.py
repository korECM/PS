class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prefix_sum: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if root:
                dfs(root.right)
                root.val, self.prefix_sum = root.val + self.prefix_sum, root.val + self.prefix_sum
                dfs(root.left)

        dfs(root)
        return root
