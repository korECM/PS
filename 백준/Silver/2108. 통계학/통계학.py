import sys
from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
nums = [0] * n
for i in range(n):
    nums[i] = num_input()
nums.sort()
print(round(sum(nums) / n))
print(nums[n // 2])
common = Counter(nums).most_common()
max_freq = common[0][1]
max_items = list(map(lambda x: x[0], filter(lambda x: x[1] == max_freq, common)))
print(sorted(max_items)[:2][-1])
print(nums[-1] - nums[0])
