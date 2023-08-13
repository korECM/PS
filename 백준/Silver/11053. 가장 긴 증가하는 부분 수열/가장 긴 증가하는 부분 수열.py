import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

n = int(input())
a = [0]
dp = [0] * (n + 1)
a.extend(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
