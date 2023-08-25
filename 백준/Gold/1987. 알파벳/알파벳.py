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

class Move:
    @staticmethod
    def generate_hv(x: int, y: int, x_range: range, y_range: range):
        """
        상하좌우 이동
        """
        g_dx, g_dy = [0, 1, -1, 0], [1, 0, 0, -1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if g_cx in x_range and g_cy in y_range:
                yield g_cx, g_cy

                
R, C = IO.nums()
board = [[ord(a) for a in IO.input()] for _ in range(R)]
alphabets = [False for _ in range(26)]
alphabets[board[0][0] - 65] = True
answer, cnt = 0, 1
words_count = 0
for b in board:
    words_count += len(set(b))

g_dx, g_dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(x: int, y: int):
    global answer, cnt
    if answer == words_count:
        return answer

    for i in range(4):
        nx, ny = x + g_dx[i], y + g_dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            alphabet = board[ny][nx] - 65
            if not alphabets[alphabet]:
                alphabets[alphabet] = True
                cnt += 1
                dfs(nx, ny)
                cnt -= 1
                alphabets[alphabet] = False

    answer = max(answer, cnt)


dfs(0, 0)

print(answer)
             

