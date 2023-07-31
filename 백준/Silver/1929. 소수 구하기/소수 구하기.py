import math
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def is_prime(num):
    if num <= 3:
        return num != 1
    if num % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


a, b = nums_input()
data = [i for i in range(a, b + 1)]
print(*filter(is_prime, data), sep='\n')
