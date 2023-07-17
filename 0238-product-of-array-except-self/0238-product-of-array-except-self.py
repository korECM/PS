from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        p = 1
        for i in range(len(nums)):
            output[i] = p
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output
