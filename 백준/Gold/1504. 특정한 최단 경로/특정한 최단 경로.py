import heapq
from collections import defaultdict
from sys import maxsize as ssm
from sys import stdin as ssi
from typing import TypeVar

MAX = ssm
hpush = heapq.heappush
hpop = heapq.heappop


class IO:
    @staticmethod
    def input() -> str: return ssi.readline().rstrip()

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


N, E = IO.nums()
graph = WeightGraph()
for _ in range(E):
    a, b, c = IO.nums()
    graph.add_bidirectional_edge(a, b, c)

v1, v2 = IO.nums()

dist = defaultdict(dict)
checked = set()


def dijkstra(start: int, end: int) -> dict[int, int]:
    if start not in checked:
        heap = [(0, start)]
        checked.add(start)
        while heap:
            time, node = hpop(heap)
            if node not in dist[start]:
                dist[start][node] = time
                for neighbor, weight in graph[node]:
                    hpush(heap, (time + weight, neighbor))
    return dist[start][end] if end in dist[start] else 200000000


answer = MAX
scenarios = [
    [1, v1, v2, N],
    [1, v2, v1, N],
]
for scenario in scenarios:
    result = 0
    for a, b in zip(scenario[:-1], scenario[1:]):
        result += dijkstra(a, b)
    answer = min(answer, result)

print(answer if answer < 200000000 else -1)
