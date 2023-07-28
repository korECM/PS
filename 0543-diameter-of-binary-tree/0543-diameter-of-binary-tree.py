from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        queue = deque([root])
        while queue:
            cur_root = queue.popleft()
            diameter = max(diameter, self.calc_diameter(cur_root))
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        return diameter

    def calc_diameter(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left_depth = right_depth = 0
        if root.left:
            left_depth = self.calc_depth(root.left)
        if root.right:
            right_depth = self.calc_depth(root.right)
        return left_depth + right_depth

    def calc_depth(selt, root: Optional[TreeNode]):
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth
