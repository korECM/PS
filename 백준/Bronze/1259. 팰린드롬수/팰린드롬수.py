import math
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())

while True:
    n = input()
    if n == "0":
        break
    print("yes" if n == n[::-1] else "no")
