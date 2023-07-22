import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


result = [i for i in range(1, 31)]
for _ in range(28):
    result.remove(num_input())
print(result[0])
print(result[1])
