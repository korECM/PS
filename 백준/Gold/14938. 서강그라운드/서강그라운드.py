from sys import maxsize as ssm
from sys import stdin as ssi
from typing import TypeVar

MAX = ssm


class IO:

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


T = TypeVar("T")


class Array:

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]


n, m, r = IO.nums()
items = [*IO.nums()]
board = Array.init_two(n, n, MAX)
for _ in range(r):
    a, b, w = IO.nums()
    board[a - 1][b - 1] = w
    board[b - 1][a - 1] = w

for i in range(n):
    board[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]

answer = 0
for i in range(n):
    count = 0
    for j in range(n):
        if board[i][j] <= m:
            count += items[j]
    answer = max(answer, count)
print(answer)
