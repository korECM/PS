import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())

a, b = nums_input()
print(a * b)
