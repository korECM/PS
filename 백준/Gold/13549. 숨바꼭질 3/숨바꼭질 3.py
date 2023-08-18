import sys
from collections import deque, defaultdict


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

a, b = nums_input()
dp = defaultdict(lambda: sys.maxsize)
dp[a] = 0
queue = deque([(a, 0)])

while queue:
    pos, time = queue.popleft()
    if pos == b:
        print(time)
        break
    if pos * 2 <= 200000 and dp[pos * 2] > time:
        dp[pos * 2] = time
        queue.appendleft((pos * 2, time))
    if pos - 1 >= 0 and dp[pos - 1] > time + 1:
        dp[pos - 1] = time + 1
        queue.append((pos - 1, time + 1))
    if pos + 1 <= 200000 and dp[pos + 1] > time + 1:
        dp[pos + 1] = time + 1
        queue.append((pos + 1, time + 1))
