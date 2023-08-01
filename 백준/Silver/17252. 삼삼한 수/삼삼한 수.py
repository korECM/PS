import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
if n == 0:
    print("NO")
else:
    i = 20
    while n and i >= 0:
        if 3 ** i <= n:
            n -= 3 ** i
        i -= 1
    print("YES" if n == 0 else "NO")
