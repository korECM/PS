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


t = num_input()
test_case = []
for _ in range(t):
    test_case.append(num_input())

max_n = max(test_case)
dp = [0, 0, 1, 1] + [0] * max_n
for i in range(4, max_n + 2):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in test_case:
    print(dp[n + 1])
