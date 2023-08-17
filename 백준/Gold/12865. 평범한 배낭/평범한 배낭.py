import sys
from collections import defaultdict


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


N, K = nums_input()
info = [(0, 0)] * N
for i in range(N):
    w, v = nums_input()
    info[i] = (w, v)

dp: dict[tuple[int, int], int] = defaultdict(int)


def solve(i: int, remain: int):
    if i < 0:
        return 0
    if (i, remain) in dp:
        return dp[(i, remain)]
    w, v = info[i]
    if w > remain:
        dp[(i, remain)] = solve(i - 1, remain)
    else:
        dp[(i, remain)] = max(solve(i - 1, remain), solve(i - 1, remain - w) + v)
    return dp[(i, remain)]


print(solve(N - 1, K))
