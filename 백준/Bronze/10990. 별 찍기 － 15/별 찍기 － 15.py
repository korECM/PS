import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
for i in range(n):
    print(" " * (n - i - 1) + "*", end='')
    if i > 0:
        print(" " * (2 * (i - 1) + 1) + "*")
    else:
        print()
