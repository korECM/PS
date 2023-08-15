import heapq
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


def init_board(height: int, width: int, init_val: T) -> list[list[T]]:
    return [[init_val for _ in range(width)] for _ in range(height)]


def print_board(board: list[list[any]]):
    for b in board:
        print(*b)


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


def create_weight_graph() -> dict[T, list[tuple[T, int]]]:
    return defaultdict(list)


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


def add_weight_directional_edge(graph: dict[T, list[tuple[T, int]]], f: T, t: T, w: int):
    graph[f].append((t, w))


v, e = nums_input()
k = num_input()
graph = create_weight_graph()
for _ in range(e):
    a, b, w = nums_input()
    add_weight_directional_edge(graph, a, b, w)

dist = {}
Q = [(0, k)]
while Q:
    d, cv = heapq.heappop(Q)
    if cv not in dist:
        dist[cv] = d
        for nv, nw in graph[cv]:
            heapq.heappush(Q, (d + nw, nv))

for i in range(1, v + 1):
    if i in dist:
        print(dist[i])
    else:
        print("INF")
