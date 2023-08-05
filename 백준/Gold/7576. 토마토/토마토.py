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

m, n = nums_input()
board = init_array(n, m, 0)
quest_tomato = 0

new_tomato = []
for i in range(n):
    board[i] = list(nums_input())
    for j in range(m):
        if board[i][j] == 1:
            new_tomato.append((j, i))
        elif board[i][j] == 0:
            quest_tomato += 1

day = 0
while new_tomato:
    temp_target = []
    for x, y in new_tomato:
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if cx < 0 or cx >= m or cy < 0 or cy >= n:
                continue
            if board[cy][cx] == 0:
                board[cy][cx] = 1
                temp_target.append((cx, cy))
                quest_tomato -= 1
    new_tomato = temp_target.copy()
    day += 1

print(day - 1 if quest_tomato == 0 else -1)
