import sys
from math import floor, ceil


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def normal_round(n):
    if n - floor(n) < 0.5:
        return floor(n)
    return ceil(n)


n = num_input()
for _ in range(n):
    print(sum(map(int, input().split(','))))
