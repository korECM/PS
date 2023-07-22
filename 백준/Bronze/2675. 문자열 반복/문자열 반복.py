import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for _ in range(n):
    n, s = input().split()
    n = int(n)
    for c in s:
        print(c * n, end='')
    print()
