import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
cards = deque([i for i in range(1, n + 1)])
while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])
