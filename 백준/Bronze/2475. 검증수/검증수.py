import sys


def input():
    return sys.stdin.readline().rstrip()


print(sum(map(lambda x: x ** 2, map(int, input().split()))) % 10)
