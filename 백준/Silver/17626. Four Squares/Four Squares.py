import math
import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

def is_square(a: int):
    if a < 1:
        return False
    return math.ceil(a ** 0.5) ** 2 == a


def check(n: int):
    if is_square(n):
        return 1
    ceil = math.ceil(n ** 0.5)
    for i in range(ceil, 0, -1):
        if is_square(n - i ** 2):
            return 2
    for i in range(ceil, 0, -1):
        for j in range(ceil, 0, -1):
            if is_square(n - i ** 2 - j ** 2):
                return 3
    return 4


print(check(num_input()))
