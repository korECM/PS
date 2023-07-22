import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')
