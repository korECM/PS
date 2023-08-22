import heapq
import sys
from collections import defaultdict
from typing import TypeVar

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

    @staticmethod
    def print(s: str): sys.stdout.write(s)

    @staticmethod
    def println(s: str): sys.stdout.write(s + '\n')


class Array:
    T = TypeVar("T")

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]

    @staticmethod
    def init_three(a: int, b: int, c: int, init_val: T) -> list[list[list[T]]]:
        return Array.init_two(a, b, [init_val for _ in range(c)])

    @staticmethod
    def print_two(board: list[list[any]]):
        for b in board: print(*b)


class Move:
    @staticmethod
    def generate_hv(x: int, y: int, x_range: range, y_range: range):
        """
        상하좌우 이동
        """
        g_dx, g_dy = [0, 1, -1, 0], [1, 0, 0, -1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if g_cx in x_range and g_cy in y_range:
                yield g_cx, g_cy

    @staticmethod
    def generate_hvd(x: int, y: int, x_range: range, y_range: range):
        """
        상하좌우 대각선 이동
        """
        g_dx, g_dy = [0, 1, -1, 0, -1, -1, 1, 1], [1, 0, 0, -1, -1, 1, -1, 1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if g_cx in x_range and g_cy in y_range:
                yield g_cx, g_cy


class Graph:
    T = TypeVar("T")
    _elem: dict[T, list[T]]

    def __init__(self):
        self._elem = defaultdict(list)

    def add_bidirectional_edge(self, a: T, b: T): self._elem[a].append(b); self._elem[b].append(a)

    def add_directional_edge(self, a: T, b: T): self._elem[a].append(b)

    def __getitem__(self, item: T) -> list[T]:
        return self._elem[item]


class WeightGraph:
    T = TypeVar("T")
    _elem: dict[T, list[tuple[T, int]]]

    def __init__(self):
        self._elem = defaultdict(list)

    def add_directional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w))

    def __getitem__(self, item: T) -> list[tuple[T, int]]:
        return self._elem[item]


N, M, X = IO.nums()
graph = WeightGraph()
for _ in range(M):
    a, b, t = IO.nums()
    graph.add_directional_edge(a, b, t)


def calc_time(a: int, b: int):
    heap = [(0, a)]
    dist = {}
    while heap:
        time, node = heapq.heappop(heap)
        if node == b:
            return time
        if node not in dist:
            dist[node] = time
            for next_node, add_time in graph[node]:
                heapq.heappush(heap, (time + add_time, next_node))


max_value = 0
for i in range(1, N + 1):
    max_value = max(max_value, calc_time(i, X) + calc_time(X, i))
print(max_value)
