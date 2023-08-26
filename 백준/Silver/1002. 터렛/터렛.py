import sys
from math import ceil, sqrt


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

def calc(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


for _ in range(IO.num()):
    x1, y1, r1, x2, y2, r2 = IO.nums()
    dist = calc(x1, y1, x2, y2)
    # 두 원 일치, 잘못 계산
    if (x1, y1) == (x2, y2):
        print(-1 if r1 == r2 else 0)
    # 외접
    elif r1 + r2 == dist:
        print(1)
    # 떨어짐
    elif r1 + r2 < dist:
        print(0)
    # 외접보다 가까이
    else:
        # 내접
        if abs(r1 - r2) == dist:
            print(1)
        # 안에서 안 만남
        elif abs(r1 - r2) > dist:
            print(0)
        else:
            print(2)


