import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
graph = {i: [] for i in range(1, n + 1)}
m = num_input()
for _ in range(m):
    a, b = nums_input()
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = set([1])
while queue:
    com = queue.popleft()
    for g in graph[com]:
        if g not in visited:
            visited.add(g)
            queue.append(g)

print(len(visited) - 1)
