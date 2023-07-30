import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()


def solve(string):
    stack = []
    for c in string:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return 'NO'
            stack.pop()
    return 'NO' if stack else 'YES'


for _ in range(n):
    print(solve(input()))
