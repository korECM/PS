import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


dp = defaultdict(list)
dp[1] = [[1]]

for i in range(2, 11):
    for d in dp[i - 1]:
        dp[i].append(d + [1])
        if d[-1] <= 2:
            dp[i].append(d[:-1] + [d[-1] + 1])

t = num_input()
for _ in range(t):
    n = num_input()
    print(len(dp[n]))
