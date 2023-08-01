import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def calc(a: int, b: int, acc: list[int]):
    if b < 0:
        return 1
    acc.append(a - b)
    return calc(b, a - b, acc) + 1


n = num_input()
prime = 1000000007
a, b, c = 0, 1, 1
for i in range(1, n):
    a, b = b, (a + b) % prime
print(b)
