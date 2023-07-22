import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
result = 1
for i in range(1, n + 1):
    result *= i
print(result)
