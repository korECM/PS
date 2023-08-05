import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
my_set = 0
all_set = 0b111111111111111111111

for _ in range(n):
    commands = input().split()
    command = commands[0]
    if command == "all":
        my_set = all_set
    elif command == "empty":
        my_set = 0
    else:
        data = int(commands[1])
        if command == "add":
            my_set |= 1 << data
        elif command == "remove":
            my_set &= ~(1 << data)
        elif command == "check":
            print(1 if my_set & (1 << data) else 0)
        elif command == "toggle":
            my_set ^= (1 << data)
