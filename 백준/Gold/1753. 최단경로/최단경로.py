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


def create_weight_graph() -> dict[T, list[tuple[T, int]]]:
    return defaultdict(list)


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
