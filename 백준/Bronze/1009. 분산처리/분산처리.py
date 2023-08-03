import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


t = num_input()
for _ in range(t):
    a, b = nums_input()
    result = 1
    for i in range(b):
        result = (result if result > 0 else 1) * a
        result %= 10
    print(result if result > 0 else 10)
