import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
deck = deque()
for _ in range(n):
    commands = input().split()
    if commands[0] == 'push_front':
        deck.appendleft(int(commands[1]))
    if commands[0] == 'push_back':
        deck.append(int(commands[1]))
    elif commands[0] == 'pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif commands[0] == 'pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(deck))
    elif commands[0] == 'empty':
        print(int(not bool(deck)))
    elif commands[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif commands[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)
