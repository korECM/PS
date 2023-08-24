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
    def print(*args: any, end: str = "\n", sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + end)

    @staticmethod
    def println(*args: any, sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + '\n')


T = TypeVar("T")

N, M = IO.nums()
target = [*IO.nums()]
target.sort()
answers = set()

def dfs(start_index: int, acc: list[int]):
    if start_index >= N:
        return
    if len(acc) == M and tuple(acc) not in answers:
        answers.add(tuple(acc))
        IO.println(*acc)
        return
    dfs(start_index, acc + [target[start_index]])
    dfs(start_index + 1, acc)


dfs(0, [])
