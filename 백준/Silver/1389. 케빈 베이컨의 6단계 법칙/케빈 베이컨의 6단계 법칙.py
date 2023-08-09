import sys
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def nums_input():
    return map(int, input().split())


T = TypeVar("T")


def init_board(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]


n, m = nums_input()
board = init_board(n + 1, n + 1, sys.maxsize)
for _ in range(m):
    a, b = nums_input()
    board[a][b] = 1
    board[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(1, n + 1):
    board[i][i] = 0

min_val, min_ind = sum(board[1][1:]), 1
for i, b in enumerate(board[2:]):
    tar_val = sum(b[1:])
    if tar_val < min_val:
        min_ind = i + 2
        min_val = tar_val
print(min_ind)
