import sys
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


dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def dfs(board: list[list[int]], visited: list[list[bool]], x: int, y: int):
    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if cx < 0 or cx >= len(board[0]) or cy < 0 or cy >= len(board):
            continue
        if not visited[cy][cx] and board[cy][cx] == 1:
            visited[cy][cx] = True
            dfs(board, visited, cx, cy)


t = num_input()
for _ in range(t):
    m, n, k = nums_input()
    board = init_array(n, m, 0)
    visited = init_array(n, m, False)
    for _ in range(k):
        x, y = nums_input()
        board[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if board[y][x] == 1 and not visited[y][x]:
                dfs(board, visited, x, y)
                count += 1
    print(count)
