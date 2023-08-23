import sys
from collections import defaultdict
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

    @staticmethod
    def print(s: str): sys.stdout.write(s)

    @staticmethod
    def println(s: str): sys.stdout.write(s + '\n')


T = TypeVar("T")


class Array:

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]

    @staticmethod
    def init_three(a: int, b: int, c: int, init_val: T) -> list[list[list[T]]]:
        return Array.init_two(a, b, [init_val for _ in range(c)])

    @staticmethod
    def print_two(board: list[list[any]]):
        for b in board: print(*b)

p = 1000000007
n = IO.num()


def mul_matrix(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    res = Array.init_two(len(mat1), len(mat2[0]), 0)
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            for k in range(len(mat2[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
                res[i][j] %= p
    return res


ans = [[1, 0], [0, 1]]
a = [[1, 1], [1, 0]]
while n:
    if n % 2 == 1:
        ans = mul_matrix(ans, a)
    a = mul_matrix(a, a)
    n //= 2
print(ans[0][1])
