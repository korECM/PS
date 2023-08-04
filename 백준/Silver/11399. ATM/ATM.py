import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
data = sorted(list(nums_input()))
print(sum(map(lambda i, e: i * e, data, range(len(data), 0, -1))))
