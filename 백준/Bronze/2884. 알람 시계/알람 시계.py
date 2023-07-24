import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


hour, minute = nums_input()
total_minute = (hour * 60 + minute - 45) % (24 * 60)
hour, minute = total_minute // 60, total_minute % 60
print(hour, minute)
