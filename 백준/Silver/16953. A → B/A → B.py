import sys
from collections import deque

class IO:
    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())


A, B = IO.nums()


def solve():
    queue = deque([(A, 1)])
    dp = {}
    while queue:
        n, t = queue.popleft()
        if n > 10 ** 9:
            continue
        if n == B:
            return t
        # if n * 2 == B:
        #     return t + 1
        # if n * 10 + 1 == B:
        #     return t + 1
        if n * 2 not in dp:
            dp[n * 2] = t + 1
            queue.append((n * 2, t + 1))
        if n * 10 + 1 not in dp:
            dp[n * 10 + 1] = t + 1
            queue.append((n * 10 + 1, t + 1))
    return -1


print(solve())
