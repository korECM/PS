class Solution:
    dp: list[int] = [0 for _ in range(50)]

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if not self.dp[n]:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
