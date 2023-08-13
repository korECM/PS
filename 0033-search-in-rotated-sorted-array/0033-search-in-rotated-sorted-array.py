import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        left_min, left_max = nums[0], nums[left]
        if left_min <= target <= left_max:
            index = bisect.bisect_left(nums[0:left + 1], target)
            if index < len(nums) and nums[index] == target:
                return index
            return -1
        else:
            index = bisect.bisect_left(nums[right:], target)
            if right + index < len(nums) and nums[right + index] == target:
                return right + index
            return -1
