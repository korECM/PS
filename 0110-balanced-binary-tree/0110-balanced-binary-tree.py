from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            return max(left_depth, right_depth) + 1

        return dfs(root) != -1
