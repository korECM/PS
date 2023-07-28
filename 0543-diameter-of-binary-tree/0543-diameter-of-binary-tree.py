from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> Tuple[int, int, int]:
            if root is None:
                return -1, -1, -1
            left_depth, _, left_max_diameter = dfs(root.left)
            right_depth, _, right_max_diameter = dfs(root.right)
            depth = max(left_depth, right_depth) + 1
            status = left_depth + right_depth + 2
            return depth, status, max(left_max_diameter, right_max_diameter, status)

        return dfs(root)[2]
