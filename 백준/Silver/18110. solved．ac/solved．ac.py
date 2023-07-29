import sys
from math import floor, ceil


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def normal_round(n):
    if n - floor(n) < 0.5:
        return floor(n)
    return ceil(n)


n = num_input()
if n == 0:
    print(0)
else:
    opinion = [0] * n
    for i in range(n):
        opinion[i] = num_input()
    opinion.sort()
    except_num = normal_round(n * 0.15)
    target = opinion[except_num:n - except_num]
    print(normal_round(sum(target) / len(target)))
