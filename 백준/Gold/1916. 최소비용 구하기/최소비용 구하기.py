from collections import defaultdict
from heapq import heappop as hpop
from heapq import heappush as hpush
from sys import stdin as ssi
from typing import TypeVar


class IO:

    @staticmethod
    def num() -> int: return int(ssi.readline())

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


T = TypeVar("T")


class WeightGraph:
    _elem: dict[T, list[tuple[T, int]]]

    def __init__(self):
        self._elem = defaultdict(list)

    def __getitem__(self, item: T) -> list[tuple[T, int]]:
        return self._elem[item]

    def __iter__(self):
        return iter(self._elem)

    def add_directional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w))

    def add_bidirectional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w));self._elem[b].append((a, w))


N, M = IO.num(), IO.num()
graph = WeightGraph()
for _ in range(M):
    a, b, w = IO.nums()
    graph.add_directional_edge(a, b, w)
s, e = IO.nums()

heap = [(0, s)]
dist = {}
while heap:
    time, node = hpop(heap)
    if node not in dist:
        dist[node] = time
        for neighbor, weight in graph[node]:
            hpush(heap, (time + weight, neighbor))
print(dist[e])
