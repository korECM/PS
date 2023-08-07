import sys
from collections import defaultdict, deque
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


T = TypeVar("T")


def init_array(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]


def move_generator(x: int, y: int,
                   x_range: range = range(0, sys.maxsize), y_range: range = range(0, sys.maxsize)):
    g_dx = [0, 1, -1, 0]
    g_dy = [1, 0, 0, -1]
    for g_i in range(4):
        g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
        if g_cx in x_range and g_cy in y_range:
            yield g_cx, g_cy


def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)


def add_bidirectional_edge(graph: dict[T, list[T]], a: T, b: T):
    graph[a].append(b)
    graph[b].append(a)


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


n, m = nums_input()
data = init_array(n, m, 0)
for i in range(n):
    for j, c in enumerate(input()):
        data[i][j] = int(c)
x, y = 0, 0
des_x, des_y = m - 1, n - 1

queue = deque([[x, y, 1]])
visited = init_array(n, m, False)
visited[y][x] = True

while queue:
    cur_x, cur_y, step = queue.popleft()
    if (cur_x, cur_y) == (des_x, des_y):
        print(step)
        break

    for nx, ny in move_generator(cur_x, cur_y, range(0, m), range(0, n)):
        if data[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append([nx, ny, step + 1])
