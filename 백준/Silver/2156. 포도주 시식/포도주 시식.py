import sys
from sys import stdin as ssi
from typing import Optional

sys.setrecursionlimit(10 ** 6)


class IO:
    @staticmethod
    def num() -> int: return int(ssi.readline())


n = IO.num()
data = [IO.num() for _ in range(n)]

mem: list[list[Optional[int]]] = [[None for _ in range(3)] for _ in range(n)]


def calc(index: int, cnt: int):
    if index >= n:
        return 0
    if mem[index][cnt] is None:
        result = 0
        # 현재 잔 마시는 경우
        if cnt > 0:
            result = max(result, calc(index + 1, cnt - 1) + data[index])
        # 안 마시고 넘기는 경우
        result = max(result, calc(index + 1, 2))
        mem[index][cnt] = result
    return mem[index][cnt]


print(calc(0, 2))
