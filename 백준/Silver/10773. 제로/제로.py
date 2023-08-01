import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


data = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(1, 15):
        data[i][j] = j if i == 0 else sum(data[i - 1][1:j + 1])

k = num_input()
data = []
for _ in range(k):
    n = num_input()
    if n == 0:
        data.pop()
    else:
        data.append(n)
print(sum(data))
