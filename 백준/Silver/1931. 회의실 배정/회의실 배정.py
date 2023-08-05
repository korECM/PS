import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
data = [[0, 0]] * n
for i in range(n):
    data[i] = list(nums_input())
count, last_time = 0, -1
for datum in sorted(data, key=lambda x: (x[1], x[0])):
    if datum[0] >= last_time:
        last_time = datum[1]
        count += 1
print(count)
