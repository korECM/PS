import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


mem = {
    1: 0,
    2: 1,
    3: 1
}
x = num_input()
for i in range(4, x + 1):
    mem[i] = min(
        mem[i // 3] + 1 if i % 3 == 0 else sys.maxsize,
        mem[i // 2] + 1 if i % 2 == 0 else sys.maxsize,
        mem[i - 1] + 1
    )
print(mem[x])
