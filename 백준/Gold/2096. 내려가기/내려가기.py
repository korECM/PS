from sys import maxsize as ssm
from sys import stdin as ssi
from typing import TypeVar

MAX = ssm


class IO:
    @staticmethod
    def num() -> int: return int(ssi.readline())

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


T = TypeVar("T")


class Array:

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]


N = IO.num()
board = [[*IO.nums()] for _ in range(N)]

min_dp = [board[0][:], board[0][:]]
max_dp = [board[0][:], board[0][:]]

for y in range(1, N):
    for x in range(3):
        cur = board[y][x]
        left, right = max(x - 1, 0), min(x + 1, 2) + 1
        min_dp[1][x] = min(min_dp[0][left:right]) + cur
        max_dp[1][x] = max(max_dp[0][left:right]) + cur
    min_dp[0] = min_dp[1][:]
    max_dp[0] = max_dp[1][:]

print(max(max_dp[-1]), min(min_dp[-1]))
