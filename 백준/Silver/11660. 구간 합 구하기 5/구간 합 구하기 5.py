import sys
from collections import defaultdict
from typing import TypeVar


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())


class Array:
    T = TypeVar("T")

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]

    @staticmethod
    def init_three(a: int, b: int, c: int, init_val: T) -> list[list[list[T]]]:
        return Array.init_two(a, b, [init_val for _ in range(c)])

    @staticmethod
    def print_two(board: list[list[any]]):
        for b in board: print(*b)

N, M = IO.nums()
board = Array.init_two(N + 2, N + 2, 0)
for y in range(N):
    for x, e in enumerate(IO.nums()):
        board[y + 1][x + 1] += e
        board[y + 2][x + 1] += board[y + 1][x + 1]
        board[y + 1][x + 2] += board[y + 1][x + 1]
        board[y + 2][x + 2] -= board[y + 1][x + 1]
operations = [[*IO.nums()] for _ in range(M)]

for a, b, c, d in operations:
    print(board[c][d] - board[c][b - 1] - board[a - 1][d] + board[a - 1][b - 1])
