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


n, m = nums_input()
max_num = -sys.maxsize
result = -sys.maxsize
board = init_board(n, m, 0)
visited = init_board(n, m, False)
for i in range(n):
    board[i] = list(nums_input())
    max_num = max(max_num, max(board[i]))


def dfs(x: int, y: int, acc: int, cnt: int):
    global result, max_num
    if cnt == 4:
        result = max(result, acc)
        return
    if result > acc + max_num * (4 - cnt):
        return
    for nx, ny in move_generator(x, y, range(0, m), range(0, n)):
        if not visited[ny][nx]:
            if cnt == 2:
                visited[ny][nx] = True
                dfs(x, y, acc + board[ny][nx], cnt + 1)
                visited[ny][nx] = False
            visited[ny][nx] = True
            dfs(nx, ny, acc + board[ny][nx], cnt + 1)
            visited[ny][nx] = False


for y in range(n):
    for x in range(m):
        visited[y][x] = True
        dfs(x, y, board[y][x], 1)
        visited[y][x] = False
print(result)
