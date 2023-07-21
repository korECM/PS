import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
