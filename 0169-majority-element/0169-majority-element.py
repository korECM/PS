from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        return [a, b][nums.count(b) > half]
