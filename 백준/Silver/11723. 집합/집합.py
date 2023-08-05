import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
my_set = set()
for _ in range(n):
    commands = input().split()
    command = commands[0]
    if command == "all":
        for i in range(1, 21):
            my_set.add(i)
    elif command == "empty":
        my_set.clear()
    else:
        data = int(commands[1])
        if command == "add":
            my_set.add(data)
        elif command == "remove":
            if data in my_set:
                my_set.remove(data)
        elif command == "check":
            print(1 if data in my_set else 0)
        elif command == "toggle":
            if data in my_set:
                my_set.remove(data)
            else:
                my_set.add(data)
