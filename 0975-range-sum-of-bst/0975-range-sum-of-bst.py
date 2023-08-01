from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if low <= root.val:
            if root.val <= high:
                return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
            else:
                return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)
