import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, k = nums_input()
result = 1
for i in range(k):
    result *= (n - i)
for i in range(1, k + 1):
    result //= i
print(result)