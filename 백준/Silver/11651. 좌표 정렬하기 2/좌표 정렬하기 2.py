import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
data = [0] * n
for i in range(n):
    x, y = nums_input()
    data[i] = (y, x)
data.sort()
print(*(map(lambda x: f'{x[1]} {x[0]}', data)), sep='\n')
