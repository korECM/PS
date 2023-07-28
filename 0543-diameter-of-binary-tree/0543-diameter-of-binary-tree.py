from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1
            left_depth, right_depth = dfs(root.left), dfs(root.right)
            self.diameter = max(self.diameter, left_depth + right_depth + 2)
            return max(left_depth, right_depth) + 1

        dfs(root)
        return self.diameter
