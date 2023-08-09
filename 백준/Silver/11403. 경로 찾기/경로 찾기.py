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


n = num_input()
board = init_board(n, n, 0)
for i in range(n):
    for j, v in enumerate(nums_input()):
        board[i][j] = v if v == 1 else sys.maxsize

for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for b in board:
    print(*map(lambda x: 1 if x < sys.maxsize else 0, b))
