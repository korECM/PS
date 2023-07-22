import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
