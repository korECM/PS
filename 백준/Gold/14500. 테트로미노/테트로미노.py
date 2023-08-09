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


target = [
    # 1
    {
        "x": [0, 1, 2, 3],
        "y": [0, 0, 0, 0]
    },
    {
        "x": [0, 0, 0, 0],
        "y": [0, 1, 2, 3]
    },
    # 2
    {
        "x": [0, 1, 0, 1],
        "y": [0, 0, 1, 1]
    },
    # 3
    {
        "x": [0, 0, 0, 1],
        "y": [0, 1, 2, 2]
    },
    {
        "x": [1, 1, 1, 0],
        "y": [0, 1, 2, 2]
    },
    {
        "x": [0, 1, 2, 2],
        "y": [1, 1, 1, 0]
    },
    {
        "x": [0, 1, 2, 2],
        "y": [0, 0, 0, 1]
    },
    {
        "x": [0, 0, 1, 2],
        "y": [1, 0, 0, 0]
    },
    {
        "x": [0, 0, 1, 2],
        "y": [0, 1, 1, 1]
    },
    {
        "x": [1, 0, 0, 0],
        "y": [0, 0, 1, 2]
    },
    {
        "x": [0, 1, 1, 1],
        "y": [0, 0, 1, 2]
    },
    # 4
    {
        "x": [0, 0, 1, 1],
        "y": [0, 1, 1, 2]
    },
    {
        "x": [1, 1, 0, 0],
        "y": [0, 1, 1, 2]
    },
    {
        "x": [0, 1, 1, 2],
        "y": [1, 1, 0, 0]
    },
    {
        "x": [0, 1, 1, 2],
        "y": [0, 0, 1, 1]
    },
    # 5
    {
        "x": [0, 1, 1, 2],
        "y": [0, 0, 1, 0],
    },
    {
        "x": [0, 0, 1, 0],
        "y": [0, 1, 1, 2]
    },
    {
        "x": [0, 1, 1, 1],
        "y": [1, 1, 0, 2]
    },
    {
        "x": [0, 1, 1, 2],
        "y": [1, 1, 0, 1]
    }
]

n, m = nums_input()
result = -sys.maxsize
board = init_board(n, m, 0)
for i in range(n):
    board[i] = list(nums_input())

for y in range(n):
    for x in range(m):
        for t in target:
            score = 0
            for i in range(4):
                tx, ty = t["x"][i], t["y"][i]
                if x + tx < 0 or x + tx >= m or y + ty < 0 or y + ty >= n:
                    score = -sys.maxsize
                    break
                score += board[y + ty][x + tx]
            result = max(result, score)
print(result)
