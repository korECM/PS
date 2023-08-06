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


n, m, v = nums_input()
graph = create_graph()
for _ in range(m):
    a, b = nums_input()
    add_bidirectional_edge(graph, a, b)


def dfs(v: int, visited: set[int], acc: list[int]):
    visited.add(v)
    acc.append(v)
    for a in sorted(graph[v]):
        if a not in visited:
            dfs(a, visited, acc)


def bfs(v: int, visited: set[int]) -> list[int]:
    acc = []
    queue = deque([v])
    visited.add(v)
    while queue:
        a = queue.popleft()
        acc.append(a)
        for b in sorted(graph[a]):
            if b not in visited:
                visited.add(b)
                queue.append(b)
    return acc


acc = []
dfs(v, set(), acc)
print(*acc)
print(*bfs(v, set()))
