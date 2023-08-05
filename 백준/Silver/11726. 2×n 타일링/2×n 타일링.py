import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


mem = {
    1: 1,
    2: 2
}
n = num_input()
for i in range(3, n + 1):
    mem[i] = (mem[i - 1] + mem[i - 2]) % 10007
print(mem[n])
