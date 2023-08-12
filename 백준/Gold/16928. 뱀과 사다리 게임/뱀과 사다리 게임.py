import sys
from collections import deque

def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())

n, m = nums_input()
data = {}
for i in range(n):
    a, b = nums_input()
    data[a] = b
for i in range(m):
    a, b = nums_input()
    data[a] = b

dp = {}
dp[1] = 0
queue = deque([(1, 0)])
while queue:
    pos, step = queue.popleft()
    for i in range(1, 7):
        new_pos, new_step = pos + i, step + 1
        if new_pos > 100:
            continue
        new_pos = new_pos if new_pos not in data else data[new_pos]
        if new_pos in dp and dp[new_pos] <= new_step:
            continue
        dp[new_pos] = new_step
        queue.append((new_pos, new_step))
print(dp[100])
