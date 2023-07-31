import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
data = [i for i in range(2666801) if '666' in str(i)]
print(data[n - 1])
