import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    print(sum([n * (n + 1) // 2 for n in (list(map(len, input().split("X"))))]))
