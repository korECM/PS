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
    age, name = input().split()
    data[i] = (int(age), i, name)
data.sort()
print(*map(lambda x: f'{x[0]} {x[2]}', data), sep='\n')
