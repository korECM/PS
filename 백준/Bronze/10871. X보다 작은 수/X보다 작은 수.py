import sys


def input():
    return sys.stdin.readline().rstrip()


n, x = map(int, input().split())
nums = map(int, input().split())
print(*[e for e in nums if e < x])