from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums) // 2
        nums.sort()
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum