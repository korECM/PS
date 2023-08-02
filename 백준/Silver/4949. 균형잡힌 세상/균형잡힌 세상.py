import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


while True:
    string = input()
    if string == ".":
        break
    stack = []
    for c in string:
        if c in "[(":
            stack.append(c)
        elif c in "]":
            if not stack or stack.pop() != "[":
                stack.append("no")
                break
        elif c in ")":
            if not stack or stack.pop() != "(":
                stack.append("no")
                break
    print("no" if stack else "yes")
