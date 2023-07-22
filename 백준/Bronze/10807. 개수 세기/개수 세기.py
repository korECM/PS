import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
nums = list(nums_input())
v = num_input()
print(nums.count(v))
