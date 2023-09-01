class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
