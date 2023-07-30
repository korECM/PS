class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prefix_sum: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.prefix_sum += root.val
            root.val = self.prefix_sum
            self.bstToGst(root.left)
        return root
