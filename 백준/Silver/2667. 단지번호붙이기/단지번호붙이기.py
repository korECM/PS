import sys
from collections import defaultdict
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


n = num_input()
data = init_array(n, n, 0)
for i in range(n):
    for j, c in enumerate(input()):
        data[i][j] = int(c)

result = []


def dfs(x: int, y: int):
    for nx, ny in move_generator(x, y, range(0, n), range(0, n)):
        if data[ny][nx] > 0:
            data[ny][nx] = -1
            result[-1] += 1
            dfs(nx, ny)


for y in range(n):
    for x in range(n):
        if data[y][x] > 0:
            data[y][x] = -1
            result.append(1)
            dfs(x, y)

print(len(result))
print(*sorted(result), sep='\n')
