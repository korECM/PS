import sys


def input():
    return sys.stdin.readline().strip()


a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
