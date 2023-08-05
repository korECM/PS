import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

n, m = nums_input()
x, y = 0, 0
data = [[0] for j in range(n)]
answer = [[sys.maxsize for j in range(m)] for i in range(n)]
for i in range(n):
    data[i] = list(nums_input())
    if 2 in data[i]:
        x, y = data[i].index(2), i
answer[y][x] = 0

queue = deque([[x, y]])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if cy < 0 or cy >= n or cx < 0 or cx >= m:
            continue
        if data[cy][cx] == 1:
            if answer[cy][cx] > answer[y][x] + 1:
                answer[cy][cx] = answer[y][x] + 1
                queue.append([cx, cy])

for y in range(n):
    for x in range(m):
        if answer[y][x] == sys.maxsize:
            answer[y][x] = 0 if data[y][x] == 0 else -1

for a in answer:
    print(*a)
