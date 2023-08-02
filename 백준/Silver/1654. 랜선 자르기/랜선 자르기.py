import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def check(data: list[int], length: int, n: int):
    for datum in data:
        n -= datum // length
    return n <= 0


k, n = nums_input()
data = [0] * k
target = set()
for i in range(k):
    data[i] = num_input()

start, end = 1, max(data) + 1
while start + 1 < end:
    mid = (start + end) // 2
    if check(data, mid, n):
        start = mid
    else:
        end = mid
print(start)
