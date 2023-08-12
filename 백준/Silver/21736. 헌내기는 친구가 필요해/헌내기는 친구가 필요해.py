import sys
from collections import deque
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())


T = TypeVar("T")


def init_board(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]


def move_generator(x: int, y: int,
                   x_range: range = range(0, sys.maxsize), y_range: range = range(0, sys.maxsize)):
    g_dx = [0, 1, -1, 0]
    g_dy = [1, 0, 0, -1]
    for g_i in range(4):
        g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
        if g_cx in x_range and g_cy in y_range:
            yield g_cx, g_cy


n, m = nums_input()
board = init_board(n, m, '')
visited = init_board(n, m, False)
s_x, s_y = 0, 0
for y in range(n):
    raw_input = input()
    for x in range(m):
        board[y][x] = raw_input[x]
        if board[y][x] == 'I':
            s_x, s_y = x, y

queue = deque([(s_x, s_y)])
answer = 0
while queue:
    x, y = queue.popleft()
    for nx, ny in move_generator(x, y, range(0, m), range(0, n)):
        if board[ny][nx] == 'X' or visited[ny][nx]:
            continue
        if board[ny][nx] == 'P':
            answer += 1
        visited[ny][nx] = True
        queue.append((nx, ny))
print(answer if answer > 0 else 'TT')
