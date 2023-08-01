import sys
from typing import Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    min_diff: int = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def get_max(node: Optional[TreeNode]):
            if not node:
                return -sys.maxsize
            if node.right:
                return get_max(node.right)
            return node.val

        def get_min(node: Optional[TreeNode]):
            if not node:
                return sys.maxsize
            if node.left:
                return get_min(node.left)
            return node.val

        def dfs(node: Optional[TreeNode]):
            if node:
                self.min_diff = min(self.min_diff, node.val - get_max(node.left), get_min(node.right) - node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.min_diff
