import sys
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


T = TypeVar("T")


def init_board(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]

for _ in range(num_input()):
    n = num_input()
    scores = init_board(2, n, 0)
    for i in range(2):
        scores[i] = [*nums_input()]
    dp = init_board(n, 3, 0)
    dp[0] = [0, scores[0][0], scores[1][0]]
    for i in range(1, n):
        # 해당 칸의 스티커를 선택하지 않는 경우
        # 이전 칸의 선택은 상관 없으므로 가장 큰 값
        dp[i][0] = max(dp[i - 1])
        # 첫 번째 칸의 스티커 선택하는 경우
        # 이전 칸에서 스티커를 선택하지 않거나, 두 번째 칸의 스티커를 고른 경우
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + scores[0][i]
        # 두 번째 칸의 스티커 선택하는 경우
        # 이전 칸에서 스티커를 선택하지 않거나, 첫 번째 칸의 스티커를 고른 경우
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + scores[1][i]
    print(max(dp[n - 1]))
