import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


nums = [0] * 10
for i in range(10):
    nums[i] = num_input()
print(sum(nums) // len(nums))
print(Counter(nums).most_common(1)[0][0])
