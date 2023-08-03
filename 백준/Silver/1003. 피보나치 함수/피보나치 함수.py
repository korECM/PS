import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


mem = {0: [1, 0], 1: [0, 1]}
for i in range(2, 41):
    a, b = mem[i - 1], mem[i - 2]
    mem[i] = [a[0] + b[0], a[1] + b[1]]
t = num_input()
for _ in range(t):
    print(*mem[num_input()])
