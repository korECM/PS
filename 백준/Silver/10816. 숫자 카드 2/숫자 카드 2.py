import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
c = Counter(nums_input())
m = num_input()
m_nums = nums_input()
result = [c[i] for i in m_nums]
print(*result)
