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
board = [[*IO.nums()] for _ in range(N)]
prefix_sum_board = Array.init_two(N, N, 0)
operations = [[*IO.nums()] for _ in range(M)]

for y in range(N):
    for x in range(N):
        prefix_sum_board[y][x] = board[y][x]
        if y > 0:
            prefix_sum_board[y][x] += prefix_sum_board[y - 1][x]
        if x > 0:
            prefix_sum_board[y][x] += prefix_sum_board[y][x - 1]
        if x > 0 and y > 0:
            prefix_sum_board[y][x] -= prefix_sum_board[y - 1][x - 1]

for a, b, c, d in operations:
    result = prefix_sum_board[c - 1][d - 1]
    if b > 1:
        result -= prefix_sum_board[c - 1][b - 2]
    if a > 1:
        result -= prefix_sum_board[a - 2][d - 1]
    if a > 1 and b > 1:
        result += prefix_sum_board[a - 2][b - 2]
    print(result)
