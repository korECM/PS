class Solution:
    dp: list[int] = [None for _ in range(0, 31)]

    def __init__(self):
        self.dp[0] = 0
        self.dp[1] = 1

    def fib(self, n: int) -> int:
        if self.dp[n] is not None:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]
