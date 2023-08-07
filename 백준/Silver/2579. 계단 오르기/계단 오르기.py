import sys
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

T = TypeVar("T")


def init_array(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]

n = num_input()
scores = [0] * n
for i in range(n):
    scores[i] = num_input()

dp = init_array(n + 2, 2, 0)
dp[2] = [scores[0], 0]

for i, score in enumerate(scores):
    if i > 0:
        dp[i + 2][0] = max(dp[i][0], dp[i][1]) + score
        dp[i + 2][1] = dp[i + 1][0] + score
print(max(dp[-1]))
