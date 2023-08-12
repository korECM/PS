import math
import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

def is_square(a: int):
    if a < 1:
        return False
    return (a ** 0.5).is_integer()


def check(n: int):
    if is_square(n):
        return 1
    square_set = {i ** 2 for i in range(int(n ** 0.5), 0, -1)}
    for i in square_set:
        if n - i in square_set:
            return 2
    for i in square_set:
        for j in square_set:
            if n - i - j in square_set:
                return 3
    return 4


print(check(num_input()))
