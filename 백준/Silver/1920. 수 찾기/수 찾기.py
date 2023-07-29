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
num_map = {k: 1 for k in nums_input()}
m = num_input()
target = nums_input()
for t in target:
    print(1 if t in num_map else 0)
