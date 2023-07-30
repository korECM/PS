from typing import List, Optional


class TreeNode:
    val: int

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None
            mid_index = len(nums) // 2
            root = TreeNode(val=nums[mid_index])
            root.left = construct(nums[:mid_index])
            root.right = construct(nums[mid_index + 1:])
            return root
        return construct(nums)
