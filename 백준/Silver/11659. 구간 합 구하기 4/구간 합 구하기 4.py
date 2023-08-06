import sys


def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())

n, m = nums_input()
data = list(nums_input())
prefix_sum = [0] * (n + 1)
for i, datum in enumerate(data):
    prefix_sum[i + 1] = prefix_sum[i] + datum

for _ in range(m):
    a, b = nums_input()
    print(prefix_sum[b] - prefix_sum[a - 1])
