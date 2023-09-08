import heapq
from collections import defaultdict
from sys import stdin as ssi
from sys import stdout as sso
from typing import TypeVar

hpush = heapq.heappush
hpop = heapq.heappop


class IO:
    @staticmethod
    def input() -> str: return ssi.readline().rstrip()

    @staticmethod
    def num() -> int: return int(ssi.readline())

    @staticmethod
    def nums(): return map(int, ssi.readline().split())

    @staticmethod
    def print(*args: any, end: str = "\n", sep: str = ' '): sso.write(sep.join(map(str, args)) + end)

    @staticmethod
    def println(*args: any, sep: str = ' '): sso.write(sep.join(map(str, args)) + '\n')


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


n = IO.num()
m = IO.num()
graph = WeightGraph()
for _ in range(m):
    a, b, w = IO.nums()
    graph.add_directional_edge(a, b, w)
start, end = IO.nums()

heap = [(0, start, None)]
dist = {}
precedence = [None for _ in range(n + 1)]
while heap:
    time, node, prev = hpop(heap)
    if node not in dist:
        dist[node] = time
        precedence[node] = prev
        if node == end:
            break
        for neighbor, weight in graph[node]:
            hpush(heap, (time + weight, neighbor, node))

path = []
node = end
while node:
    path.append(node)
    node = precedence[node]
IO.println(dist[end])
IO.println(len(path))
IO.println(*path[::-1])
