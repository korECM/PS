import math
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    n = input()
    if n == "0":
        break
    print("yes" if n == n[::-1] else "no")
