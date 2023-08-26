from collections import deque

A, B = map(int, input().split())

def solve():
    queue = deque([(A, 1)])
    dp = {}
    while queue:
        n, t = queue.popleft()
        if n > 10 ** 9:
            continue
        if n == B:
            return t
        if n * 2 not in dp:
            dp[n * 2] = t + 1
            queue.append((n * 2, t + 1))
        if n * 10 + 1 not in dp:
            dp[n * 10 + 1] = t + 1
            queue.append((n * 10 + 1, t + 1))
    return -1


print(solve())
