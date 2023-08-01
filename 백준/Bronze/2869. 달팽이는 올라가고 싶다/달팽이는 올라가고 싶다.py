import sys
from math import ceil


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


a, b, v = nums_input()
day = 1
day_offset = a - b
print(day * ceil((v - a) / day_offset) + 1)
