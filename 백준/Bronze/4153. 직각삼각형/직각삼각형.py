import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


while True:
    a, b, c = sorted(nums_input())
    if c == 0:
        break
    print("right" if a ** 2 + b ** 2 == c ** 2 else "wrong")
