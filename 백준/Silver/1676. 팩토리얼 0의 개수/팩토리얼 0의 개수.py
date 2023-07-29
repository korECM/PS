import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
result, mul = 0, 1
for i in range(1, n + 1):
    mul *= i
    k = 0
    while mul % (10 ** (k + 1)) == 0:
        k += 1
    mul //= 10 ** k
    result += k
print(result)
