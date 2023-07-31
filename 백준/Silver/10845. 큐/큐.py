import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
queue = deque()
for _ in range(n):
    commands = input().split()
    if commands[0] == 'push':
        queue.append(int(commands[1]))
    elif commands[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        print(int(not bool(queue)))
    elif commands[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commands[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
