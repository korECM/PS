import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, k = nums_input()
result = 0
t = [0] * n
for i in range(n):
    t[i] = num_input()

for i in range(n - 1, -1, -1):
    result += k // t[i]
    k %= t[i]
    if k == 0:
        break
print(result)
