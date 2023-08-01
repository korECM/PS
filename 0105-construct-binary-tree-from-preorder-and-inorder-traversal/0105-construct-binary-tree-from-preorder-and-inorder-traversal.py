from typing import Optional, List


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        parent = preorder[0]
        parent_index = inorder.index(parent)
        left_inorder_part = inorder[:parent_index]
        right_inorder_part = inorder[parent_index + 1:]
        left_preorder_part = preorder[1:1 + len(left_inorder_part)]
        right_preorder_part = preorder[1 + len(left_inorder_part):]
        return TreeNode(val=parent, left=self.buildTree(left_preorder_part, left_inorder_part),
                        right=self.buildTree(right_preorder_part, right_inorder_part))
