import sys


def input():
    return sys.stdin.readline().strip()


a, b, c = map(int, input().split())
print(a + b + c)
