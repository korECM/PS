import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
d = defaultdict(int)
for i in range(n):
    d[num_input()] += 1
for k in sorted(d.keys()):
    for _ in range(d[k]):
        print(k)
