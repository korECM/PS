import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

password = {}
m, n = nums_input()
for _ in range(m):
    a, b = input().split()
    password[a] = b
for _ in range(n):
    print(password[input()])
