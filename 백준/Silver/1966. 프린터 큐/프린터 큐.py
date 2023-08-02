import heapq
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
    pq = []
    for i, p in enumerate(nums_input()):
        queue.append((-p, i))
        heapq.heappush(pq, -p)
    count = 1
    while True:
        item = queue.popleft()
        next_target = heapq.heappop(pq)
        if item[0] != next_target:
            queue.append(item)
            heapq.heappush(pq, next_target)
        elif item[1] == m:
            print(count)
            break
        else:
            count += 1
