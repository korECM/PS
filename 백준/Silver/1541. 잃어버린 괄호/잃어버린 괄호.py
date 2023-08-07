import re
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


def move_generator2(x: int, y: int, z: int,
                    x_range: range = range(0, sys.maxsize), y_range: range = range(0, sys.maxsize),
                    z_range: range = range(0, sys.maxsize)):
    g_dx = [0, 1, -1, 0, 0, 0]
    g_dy = [1, 0, 0, -1, 0, 0]
    g_dz = [0, 0, 0, 0, 1, -1]
    for g_i in range(6):
        g_cx, g_cy, g_cz = x + g_dx[g_i], y + g_dy[g_i], z + g_dz[g_i]
        if g_cx in x_range and g_cy in y_range and g_cz in z_range:
            yield g_cx, g_cy, g_cz


def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)


def add_bidirectional_edge(graph: dict[T, list[T]], a: T, b: T):
    graph[a].append(b)
    graph[b].append(a)


def add_directional_edge(graph: dict[T, list[T]], f: T, t: T):
    graph[f].append(t)


split_input = re.split('(\\d+)', input())[1:-1]
operands, operators = list(map(int, split_input[::2])), split_input[1::2]

sum = operands[0]
temp_sum = 0
for op, operand in zip(operators, operands[1:]):
    if op == "+":
        if temp_sum:
            temp_sum += operand
        else:
            sum += operand
    else:
        temp_sum += operand
print(sum - temp_sum)
