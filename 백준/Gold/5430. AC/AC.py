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


class NewArray:
    data: list[str]
    front_index: int
    back_index: int
    is_reversed: bool

    def __init__(self, data: list[str]):
        self.data = data
        self.is_reversed = False
        self.front_index = 0
        self.back_index = len(data)

    def reverse(self):
        self.is_reversed = not self.is_reversed

    def pop(self):
        if self.is_reversed:
            self.back_index -= 1
        else:
            self.front_index += 1

    def get_data(self):
        direct_ = self.data[self.front_index:self.back_index] \
            if not self.is_reversed \
            else self.data[self.back_index - 1:None if self.front_index == 0 else self.front_index - 1:-1]
        return f"[{','.join(direct_)}]"


t = num_input()
for _ in range(t):
    func = input()
    n = num_input()
    raw_input = input()[1:-1].replace("RR", "")
    array = NewArray(list(raw_input.split(',')) if n > 0 else [])
    if func.count("D") > n:
        print("error")
        continue
    for f in func:
        if f == "R":
            array.reverse()
        else:
            array.pop()
    print(array.get_data())
