import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


k = num_input()
data = []
for _ in range(k):
    n = num_input()
    if n == 0:
        data.pop()
    else:
        data.append(n)
print(sum(data))
