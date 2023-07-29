import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
for i in range(1, n + 1):
    a, b = nums_input()
    print(f"Case #{i}: {a} + {b} = {a + b}")
