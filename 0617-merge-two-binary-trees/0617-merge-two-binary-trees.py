from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
            if r1 is None or r2 is None:
                return r1 if r1 else r2
            r1.val += r2.val
            r1.left = merge(r1.left, r2.left)
            r1.right = merge(r1.right, r2.right)
            return r1

        return merge(root1, root2)
