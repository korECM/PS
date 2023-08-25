import sys
from collections import defaultdict, deque
from itertools import combinations
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
    def print(*args: any, end: str = "\n", sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + end)

    @staticmethod
    def println(*args: any, sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + '\n')


T = TypeVar("T")

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

N, M = IO.nums()
board: list[list[int]] = [[*IO.nums()] for _ in range(N)]
org_safe_area = -3
virus_pos: list[tuple[int, int]] = []
blanks = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            blanks.append((x, y))
            org_safe_area += 1
        elif board[y][x] == 2:
            virus_pos.append((x, y))

answer = 0


def calc(new_wall: list[tuple[int, int]]) -> int:
    queue = deque(virus_pos)
    visited = set(virus_pos + new_wall)
    new_virus_count = 0
    while queue:
        x, y = queue.popleft()
        for nx, ny in Move.generate_hv(x, y, range(0, M), range(0, N)):
            if (nx, ny) not in visited and board[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
                new_virus_count += 1
        if answer > 0 and org_safe_area - new_virus_count < answer:
            new_virus_count += 1000000
            break
    return org_safe_area - new_virus_count


def check():
    global answer
    for walls in combinations(blanks, 3):
        answer = max(answer, calc(list(walls)))


check()
print(answer)
