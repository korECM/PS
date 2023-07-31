import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, m = nums_input()
nums = list(nums_input())
print(max(filter(lambda x: x <= m, map(sum, combinations(nums, 3)))))
