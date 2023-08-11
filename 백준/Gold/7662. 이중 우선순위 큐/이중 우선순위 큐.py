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


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


t = num_input()
for _ in range(t):
    deleted_set = set()
    count = 0
    k = num_input()
    min_heap, max_heap = [], []
    for _ in range(k):
        raw_input = input().split()
        a, b = raw_input[0], int(raw_input[1])
        if a == "I":
            heapq.heappush(min_heap, (b, count))
            heapq.heappush(max_heap, (-b, count))
            count += 1
        else:
            if b == 1:
                while max_heap:
                    _, i = heapq.heappop(max_heap)
                    if i not in deleted_set:
                        deleted_set.add(i)
                        break
            else:
                while min_heap:
                    _, i = heapq.heappop(min_heap)
                    if i not in deleted_set:
                        deleted_set.add(i)
                        break
    while min_heap:
        a, i = heapq.heappop(min_heap)
        if i not in deleted_set:
            heapq.heappush(min_heap, (a, i))
            break
    while max_heap:
        a, i = heapq.heappop(max_heap)
        if i not in deleted_set:
            heapq.heappush(max_heap, (a, i))
            break
    if not min_heap:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
