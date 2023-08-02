import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
data = []
for i in range(n):
    data.append(list(nums_input()))
print(*[len([y for y in data if y[0] > x[0] and y[1] > x[1]]) + 1 for x in data])
