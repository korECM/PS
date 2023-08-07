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


def move_generator2(x: int, y: int, z: int,
                    x_range: range = range(0, sys.maxsize), y_range: range = range(0, sys.maxsize),
                    z_range: range = range(0, sys.maxsize)):
    g_dx = [0, 1, -1, 0, 0, 0]
    g_dy = [1, 0, 0, -1, 0, 0]
    g_dz = [0, 0, 0, 0, 1, -1]
    for g_i in range(6):
        g_cx, g_cy, g_cz = x + g_dx[g_i], y + g_dy[g_i], z + g_dz[g_i]
        if g_cx in x_range and g_cy in y_range and g_cz in z_range:
            yield g_cx, g_cy, g_cz


def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)


def add_bidirectional_edge(graph: dict[T, list[T]], a: T, b: T):
    graph[a].append(b)
    graph[b].append(a)


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


m, n, h = nums_input()
quest_count = 0
queue = deque()
data = [[
    [0 for _ in range(m)]
    for _ in range(n)
] for _ in range(h)]
for z in range(h):
    for y in range(n):
        for x, v in enumerate(nums_input()):
            data[z][y][x] = v
            if v == 0:
                quest_count += 1
            elif v == 1:
                queue.append([x, y, z])

day = -1
while queue:
    temp = []
    for _ in range(len(queue)):
        x, y, z = queue.popleft()
        for nx, ny, nz in move_generator2(x, y, z, range(0, m), range(0, n), range(0, h)):
            if data[nz][ny][nx] == 0:
                temp.append([nx, ny, nz])
                data[nz][ny][nx] = 1
                quest_count -= 1
    queue.extend(temp)
    day += 1
print(day if quest_count == 0 else -1)
