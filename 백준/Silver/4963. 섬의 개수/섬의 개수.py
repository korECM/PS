from collections import deque
from sys import stdin as ssi
from sys import stdout as sso


class IO:

    @staticmethod
    def nums(): return map(int, ssi.readline().split())

    @staticmethod
    def println(*args: any, sep: str = ' '): sso.write(sep.join(map(str, args)) + '\n')


class Move:

    @staticmethod
    def generate_hvd(x: int, y: int, x_low: int, x_high: int, y_low: int, y_high: int):
        """
        상하좌우 대각선 이동
        """
        g_dx, g_dy = [0, 1, -1, 0, -1, -1, 1, 1], [1, 0, 0, -1, -1, 1, -1, 1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if x_low <= g_cx < x_high and y_low <= g_cy < y_high:
                yield g_cx, g_cy


def calc(board: list[list[int]], x: int, y: int, visited: set[tuple[int, int]]):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for nx, ny in Move.generate_hvd(cx, cy, 0, len(board[0]), 0, len(board)):
            if (nx, ny) not in visited and board[ny][nx]:
                visited.add((nx, ny))
                queue.append((nx, ny))


while True:
    w, h = IO.nums()
    if w == 0 and h == 0:
        break
    board = [[*IO.nums()] for _ in range(h)]
    count = 0
    visited = set()
    for y in range(h):
        for x in range(w):
            if board[y][x] and (x, y) not in visited:
                visited.add((x, y))
                calc(board, x, y, visited)
                count += 1

    IO.println(count)
