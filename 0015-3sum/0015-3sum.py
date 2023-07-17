from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return solution
