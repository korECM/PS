import bisect
import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
a = [0]
dp = [0]
a.extend(nums_input())

for i in range(1, n + 1):
    if dp[-1] < a[i]:
        dp.append(a[i])
    else:
        index = bisect.bisect_left(dp, a[i])
        dp[index] = a[i]
print(len(dp) - 1)
