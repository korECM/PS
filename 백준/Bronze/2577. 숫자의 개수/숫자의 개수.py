import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


counter = Counter(str(num_input() * num_input() * num_input()))
for x in range(10):
    print(counter[str(x)])
