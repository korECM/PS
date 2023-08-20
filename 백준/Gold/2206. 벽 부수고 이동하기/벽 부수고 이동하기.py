import sys
from collections import deque
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


def init_cube(height: int, width: int, depth: int, init_val: T) -> list[list[list[T]]]:
    return [[[init_val for _ in range(depth)] for _ in range(width)] for _ in range(height)]

def move_generator(x: int, y: int,
                   x_range: range = range(0, sys.maxsize), y_range: range = range(0, sys.maxsize)):
    g_dx = [0, 1, -1, 0]
    g_dy = [1, 0, 0, -1]
    for g_i in range(4):
        g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
        if g_cx in x_range and g_cy in y_range:
            yield g_cx, g_cy


N, M = nums_input()
board = init_board(N + 1, M + 1, 0)
for i in range(1, N + 1):
    board[i] = [0] + list(map(int, input()))

dist = init_cube(N + 1, M + 1, 2, sys.maxsize)
queue = deque([(1, 1, 1, 0)])
dist[1][1][0] = 1
while queue:
    x, y, step, bomb_count = queue.popleft()
    if x == M and y == N:
        break
    for nx, ny in move_generator(x, y, range(1, M + 1), range(1, N + 1)):
        target_cell = dist[ny][nx]
        if board[ny][nx] == 0 and target_cell[bomb_count] > step + 1:
            target_cell[bomb_count] = step + 1
            queue.append((nx, ny, step + 1, bomb_count))
        elif bomb_count == 0 and target_cell[1] > step + 1:
            target_cell[1] = step + 1
            queue.append((nx, ny, step + 1, 1))
print(min(dist[N][M]) if min(dist[N][M]) != sys.maxsize else -1)
