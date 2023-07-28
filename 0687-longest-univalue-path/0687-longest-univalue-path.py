from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    dist: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], prev_val: int):
            if root is None:
                return 0

            left_dist = dfs(root.left, root.val)
            right_dist = dfs(root.right, root.val)
            self.dist = max(self.dist, left_dist + right_dist)
            if root.val == prev_val:
                return max(left_dist, right_dist) + 1
            else:
                return 0

        dfs(root, -1)
        return self.dist
