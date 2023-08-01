from typing import Optional, List


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        parent = preorder.pop(0)
        parent_index = inorder.index(parent)
        return TreeNode(val=parent,
                        left=self.buildTree(preorder, inorder[:parent_index]),
                        right=self.buildTree(preorder, inorder[parent_index + 1:])
                        )
