import sys


def input():
    return sys.stdin.readline().rstrip()


s = input()
n = int(input())
print(s[n - 1])
