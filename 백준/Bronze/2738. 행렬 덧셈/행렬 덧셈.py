import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, m = nums_input()
a, b = [], []
for _ in range(n):
    a.append(list(nums_input()))
for _ in range(n):
    b.append(list(nums_input()))

for y in range(n):
    for x in range(m):
        print(a[y][x] + b[y][x], end=' ')
    print()
