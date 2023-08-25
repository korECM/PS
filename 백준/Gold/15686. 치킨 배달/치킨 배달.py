import sys
from collections import defaultdict
from itertools import combinations
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())


N, M = IO.nums()
board = [[*IO.nums()] for _ in range(N)]
chickens: list[tuple[int, int]] = []
houses: list[tuple[int, int]] = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 2:
            chickens.append((x, y))
        elif board[y][x] == 1:
            houses.append((x, y))

answer = MAX


def calc_dist(a: tuple[int, int], b: tuple[int, int]):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calc(sc: list[tuple[int, int]]):
    chicken_distance = 0
    for house in houses:
        house_chicken_distance = MAX
        for chicken in sc:
            house_chicken_distance = min(house_chicken_distance, calc_dist(house, chicken))
        chicken_distance += house_chicken_distance
    return chicken_distance


for surviving_chickens in combinations(chickens, M):
    answer = min(answer, calc(surviving_chickens))
print(answer)
