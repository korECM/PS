import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


s = input()
result = []
for c in range(ord('a'), ord('z') + 1):
    result.append(s.find(chr(c)))
print(*result)
