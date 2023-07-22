import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


while True:
    s = input()
    if not s:
        break
    print(s)
