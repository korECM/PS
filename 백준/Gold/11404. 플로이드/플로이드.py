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

n, m = IO.num(), IO.num()
board = Array.init_two(n + 1, n + 1, sys.maxsize)
for _ in range(m):
    a, b, c = IO.nums()
    board[a][b] = min(board[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                board[a][b] = min(board[a][b], board[a][k] + board[k][b])

output = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        output.append(board[i][j] if board[i][j] != sys.maxsize else 0)
    print(*output)
    output.clear()
