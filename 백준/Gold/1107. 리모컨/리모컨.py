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


cur_channel = 100
n, m = num_input(), num_input()
str_n = str(n)
min_value = abs(n - cur_channel)


def solve(n: int, data: set[int], acc: str):
    global min_value
    if acc and len(acc) > 6:
        return
    if acc:
        min_value = min(min_value, abs(n - int(acc)) + len(acc))
    for datum in data:
        solve(n, data, acc + str(datum))


if m == 10:
    print(abs(n - cur_channel))
elif m == 0:
    print(min(abs(n - cur_channel), len(str(n))))
else:
    data = set(range(0, 10)) - set(nums_input())
    solve(n, data, "")
    print(min_value)
