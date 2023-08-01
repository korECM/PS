import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(1, n):
    print(" " * i + "*" * (2 * (n - i - 1) + 1))
