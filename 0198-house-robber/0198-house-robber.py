class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])
