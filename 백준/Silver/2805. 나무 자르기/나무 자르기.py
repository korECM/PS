import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def check(trees: list[int], m: int, height: int):
    return sum(map(lambda x: max(x - height, 0), trees)) >= m


n, m = nums_input()
trees = list(nums_input())
start, end = 0, max(trees)
while start + 1 < end:
    mid = (start + end) // 2
    if check(trees, m, mid):
        start = mid
    else:
        end = mid
print(start)
