import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
