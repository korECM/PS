import sys
from collections import defaultdict, deque
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
org_safe_area = N * M
virus_pos: list[tuple[int, int]] = []
for y in range(N):
    for x in range(M):
        if board[y][x] != 0:
            org_safe_area -= 1
        if board[y][x] == 2:
            virus_pos.append((x, y))

answer = 0


def calc(new_wall: list[tuple[int, int]]) -> int:
    new_virus = []
    should_calc = True
    queue = deque(virus_pos)
    while queue:
        x, y = queue.popleft()
        for nx, ny in Move.generate_hv(x, y, range(0, M), range(0, N)):
            if (nx, ny) not in new_wall and board[ny][nx] == 0:
                board[ny][nx] = 2
                new_virus.append((nx, ny))
                queue.append((nx, ny))
        if answer > 0 and org_safe_area - len(new_virus) - 3 < answer:
            should_calc = False
            break
    for x, y in new_virus:
        board[y][x] = 0
    return 0 if not should_calc else org_safe_area - len(new_virus) - 3


def check(new_wall: list[tuple[int, int]]):
    global answer
    if len(new_wall) == 4:
        answer = max(answer, calc(new_wall[1:]))
        return

    last_x, last_y = new_wall[-1]
    for x in range(last_x + 1, M):
        if board[max(last_y, 0)][x] == 0:
            check(new_wall + [(x, max(last_y, 0))])
    for y in range(last_y + 1, N):
        for x in range(M):
            if board[y][x] == 0:
                check(new_wall + [(x, y)])


check([(-1, -1)])
print(answer)
