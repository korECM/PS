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

def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)

def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


n = num_input()
graph = create_graph()
for i in range(n):
    for j, v in enumerate(nums_input()):
        if v == 1:
            add_directional_edge(graph, i, j)

dp = init_board(n, n, False)
for i in range(n):
    heap = [(0, i)]
    dist = {}
    while heap:
        d, v = heapq.heappop(heap)
        if d != 0:
            dp[i][v] = True
        if v not in dist:
            dist[v] = d
            for nv in graph[v]:
                heapq.heappush(heap, (d + 1, nv))

for i in range(n):
    print(*map(lambda j: 1 if dp[i][j] else 0, range(n)))
