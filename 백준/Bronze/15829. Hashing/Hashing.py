import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


r = 31
m = 1234567891
l = num_input()
str = map(lambda x: ord(x) - ord('a') + 1, list(input()))
result = 0
for i, c in enumerate(str):
    result += (((r ** i) % m) * c) % m
print(result)
