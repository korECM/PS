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


def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)


def add_bidirectional_edge(graph: dict[T, list[T]], a: T, b: T):
    graph[a].append(b)
    graph[b].append(a)


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


n = num_input()
board = init_board(n, n, '')
for i in range(n):
    board[i] = [*input()]


def bfs(org_x: int, org_y: int, visited: list[list[bool]], matching: dict[str, list[str]]):
    queue = deque([(org_x, org_y)])
    visited[org_y][org_x] = True
    while queue:
        x, y = queue.popleft()
        for nx, ny in move_generator(x, y, range(0, n), range(0, n)):
            if not visited[ny][nx] and board[ny][nx] in matching[board[y][x]]:
                visited[ny][nx] = True
                queue.append((nx, ny))


visited = init_board(n, n, False)
count_1 = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            count_1 += 1
            bfs(x, y, visited, {'R': ['R'], 'G': ['G'], 'B': ['B']})
visited = init_board(n, n, False)
count_2 = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            visited[y][x] = True
            count_2 += 1
            bfs(x, y, visited, {'R': ['R', 'G'], 'G': ['R', 'G'], 'B': ['B']})
print(count_1, count_2)
