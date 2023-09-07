from collections import deque
from sys import stdin as ssi
from typing import TypeVar


class IO:

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


T = TypeVar("T")


class Move:
    @staticmethod
    def generate_hv(x: int, y: int, x_low: int, x_high: int, y_low: int, y_high: int):
        """
        상하좌우 이동
        """
        g_dx, g_dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if x_low <= g_cx < x_high and y_low <= g_cy < y_high:
                yield g_cx, g_cy


N, M = IO.nums()
board: list[list[int]] = [[*IO.nums()] for _ in range(N)]


def find_candidates():
    target_candidates = set()
    queue = deque([(0, 0)])
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while queue:
        x, y = queue.popleft()
        for nx, ny in Move.generate_hv(x, y, 0, M, 0, N):
            if visited[ny][nx] >= 2:
                continue
            if board[ny][nx]:
                visited[ny][nx] += 1
                if visited[ny][nx] == 2:
                    target_candidates.add((nx, ny))
            else:
                visited[ny][nx] += 2
                queue.append((nx, ny))
    return target_candidates


def is_target(x: int, y: int):
    if board[y][x] == 0:
        return False
    count = 0
    for nx, ny in Move.generate_hv(x, y, 0, M, 0, N):
        if board[ny][nx] == 0:
            count += 1
    return count >= 2


time = 0
while True:
    targets = []
    for x, y in find_candidates():
        if is_target(x, y):
            targets.append((x, y))

    if not targets:
        break

    for x, y in targets:
        board[y][x] = 0
    time += 1
print(time)
