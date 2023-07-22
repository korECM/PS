import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
s = input()
result = 0
for c in s:
    result += int(c)
print(result)
