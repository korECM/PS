import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


get_average = lambda l: sum(l) / len(l)

n = num_input()
scores = list(nums_input())
max_score = max(scores)
print(get_average([s / max_score * 100 for s in scores]))
