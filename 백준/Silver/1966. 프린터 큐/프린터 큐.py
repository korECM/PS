import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


t = num_input()
for _ in range(t):
    n, m = nums_input()
    queue = deque()
    p = [0] * n
    for i, priority in enumerate(nums_input()):
        queue.append((priority, i))
        p[i] = priority
    p.sort()
    count = 1
    while True:
        item = queue.popleft()
        next_target = p[-1]
        if item[0] != next_target:
            queue.append(item)
        elif item[1] == m:
            p.pop()
            print(count)
            break
        else:
            p.pop()
            count += 1
