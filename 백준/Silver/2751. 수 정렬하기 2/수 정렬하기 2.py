import sys


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
for num in nums:
    print(num)
