import sys
from collections import defaultdict, deque
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


n, m = nums_input()
data = {}
for i in range(n):
    a, b = nums_input()
    data[a] = b
for i in range(m):
    a, b = nums_input()
    data[a] = b

dp = {}
dp[1] = 0
queue = deque([(1, 0)])
while queue:
    pos, step = queue.popleft()
    for i in range(1, 7):
        new_pos, new_step = pos + i, step + 1
        if new_pos > 100:
            continue
        new_pos = new_pos if new_pos not in data else data[new_pos]
        if new_pos in dp and dp[new_pos] <= new_step:
            continue
        dp[new_pos] = new_step
        queue.append((new_pos, new_step))
print(dp[100])
