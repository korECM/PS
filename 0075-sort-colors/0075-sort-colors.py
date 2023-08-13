from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        first, last = 0, len(nums) - 1
        index = 0
        while index < len(nums) and last >= 0 and first < len(nums):
            if nums[index] == 2 and index < last:
                nums[index], nums[last] = nums[last], nums[index]
                last -= 1
            elif nums[index] == 0 and index > first:
                nums[index], nums[first] = nums[first], nums[index]
                first += 1
            else:
                index += 1
