import sys
from collections import defaultdict
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

    @staticmethod
    def print(s: str): sys.stdout.write(s)

    @staticmethod
    def println(s: str): sys.stdout.write(s + '\n')

def check(n: int, c: int):
    while n > 1:
        if n % c != 0:
            return False
        n //= c
    return True


def find(p: int):
    a, b = 1, 1
    if p == 2:
        return 3
    seq = 2
    while True:
        a = (a + b) % p
        b = (a + b) % p
        if a == 1 and b == 1:
            return seq
        seq += 2


def fast_find(p: int) -> tuple[bool, int]:
    if check(p, 2):
        return True, 3 * p // 2
    elif check(p, 5):
        return True, 4 * p
    elif p % 2 == 0 and check(p // 2, 5):
        return True, 6 * p
    elif p > 100 and check(p, 10):
        return True, 15 * (p // 10)
    return False, 0


for _ in range(IO.num()):
    a, n = IO.nums()
    success, result = fast_find(n)
    if success:
        print(a, result)
    else:
        print(a, find(n))

