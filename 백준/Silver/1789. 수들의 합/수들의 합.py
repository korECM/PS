import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
count = 0
index = 1
while True:
    count += index
    if count > n:
        index -= 1
    if count >= n:
        break
    index += 1
print(index)
