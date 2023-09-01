class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[0, 0] for _ in range(max(3, n + 1))]
        dp[1] = [1, 0]
        dp[2] = [1, 1]
        for i in range(3, n + 1):
            # 한 칸
            dp[i][0] = dp[i - 1][1] + sum(dp[i - 2])
            # 두 칸
            dp[i][1] = sum(dp[i - 2])
        return sum(dp[n])
