import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


nums = list(nums_input())
if nums == sorted(nums):
    print("ascending")
elif nums == sorted(nums, reverse=True):
    print("descending")
else:
    print("mixed")
