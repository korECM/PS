import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

t = num_input()
test_case = []
for _ in range(t):
    test_case.append(num_input())

max_n = max(test_case)
dp = [0, 0, 1, 1] + [0] * max_n
for i in range(4, max_n + 2):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in test_case:
    print(dp[n + 1])
