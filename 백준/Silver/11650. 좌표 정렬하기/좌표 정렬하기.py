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
    data[i] = list(nums_input())
data.sort()
print(*(map(' '.join, map(lambda x: list(map(str, x)), data))), sep='\n')
