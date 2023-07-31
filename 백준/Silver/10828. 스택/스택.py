import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
stack = []
for _ in range(n):
    commands = input().split()
    if commands[0] == 'push':
        stack.append(int(commands[1]))
    elif commands[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(stack))
    elif commands[0] == 'empty':
        print(int(not bool(stack)))
    elif commands[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
