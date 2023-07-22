import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


grade_map = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0.0,
    "+": 0.3,
    "-": -0.3,
    "0": 0.0
}

grade = input()
result = 0
if grade == "F":
    print(0.0)
else:
    print(grade_map[grade[0]] + grade_map[grade[1]])
