import sys
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


n = num_input()
board = init_board(n, n, False)
row_check = set()
queen_position = set()

answer = 0


def solve(column: int):
    global answer
    if column == n:
        answer += 1
        return

    # 열 선택
    for row in range(n):
        if row in row_check:
            continue

        flag = False
        for nc, nr in queen_position:
            if abs(column - nc) == abs(row - nr):
                flag = True
                break
        if flag:
            continue

        queen_position.add((column, row))
        row_check.add(row)
        solve(column + 1)
        row_check.remove(row)
        queen_position.remove((column, row))

solve(0)
print(answer)
