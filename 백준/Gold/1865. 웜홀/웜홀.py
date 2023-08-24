import sys
from collections import defaultdict
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

T = TypeVar("T")

class WeightGraph:
    _elem: dict[T, list[tuple[T, int]]]

    def __init__(self):
        self._elem = defaultdict(list)

    def add_directional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w))

    def add_bidirectional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w));self._elem[b].append((a, w))

    def __getitem__(self, item: T) -> list[tuple[T, int]]:
        return self._elem[item]

    def __iter__(self):
        return iter(self._elem)

def bellman_ford(graph: WeightGraph, start: int) -> tuple[bool, dict[int, int]]:
    distance = defaultdict(lambda: sys.maxsize)
    distance[start] = 0
    for _ in range(N - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distance[neighbor] > distance[node] + weight:
                    distance[neighbor] = distance[node] + weight

    for node in graph:
        for neighbor, weighVt in graph[node]:
            if distance[neighbor] > distance[node] + weighVt:
                return True, dict()

    return False, distance


for _ in range(IO.num()):
    N, M, W = IO.nums()
    graph = WeightGraph()
    for _ in range(M):
        s, e, t = IO.nums()
        graph.add_bidirectional_edge(s, e, t)
    for _ in range(W):
        s, e, t = IO.nums()
        graph.add_directional_edge(s, e, -t)
    cycle, dist = bellman_ford(graph, 1)
    print("YES" if cycle else "NO")
