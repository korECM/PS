from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    flag: bool = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not self.flag or root is None:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if abs(left_depth - right_depth) > 1:
                self.flag = False
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.flag
