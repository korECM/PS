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


n = num_input()
s = 1
for i in range(1, 1020000):
    if n <= s:
        print(i)
        break
    s += 6 * i
