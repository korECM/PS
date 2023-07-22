import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


target = set()
for _ in range(10):
    target.add(num_input() % 42)
print(len(target))
