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


n = num_input()
data = [[0]] * n
for i in range(n):
    data[i] = list(nums_input())

result = [0, 0]


def dfs(left: int, up: int, n: int):
    if n == 0:
        return
    if all([all(x == 1 for x in y[left: left + n]) for y in data[up:up + n]]):
        result[1] += 1
        return
    elif all([all(x == 0 for x in y[left: left + n]) for y in data[up:up + n]]):
        result[0] += 1
        return
    dfs(left, up, n // 2)
    dfs(left, up + n // 2, n // 2)
    dfs(left + n // 2, up, n // 2)
    dfs(left + n // 2, up + n // 2, n // 2)


dfs(0, 0, n)
print(result[0])
print(result[1])
