import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


while True:
    a, b = nums_input()
    if (a, b) == (0, 0):
        break
    print("Yes" if a > b else "No")
