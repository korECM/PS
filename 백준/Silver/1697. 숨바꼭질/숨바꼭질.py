import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, k = nums_input()
mem = {
    n: 0,
    k: abs(n - k)
}

if n < k:
    queue = deque([(n + 1, n), (n - 1, n), (2 * n, n)])
    while queue:
        cur, prev = queue.popleft()
        if cur < 0 or cur > 100000:
            continue
        if mem[prev] >= mem[k]:
            continue
        if cur in mem and mem[cur] < mem[prev] + 1:
            continue

        mem[cur] = mem[prev] + 1
        queue.extend([(cur + 1, cur), (cur - 1, cur), (cur * 2, cur)])
print(mem[k])
