import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
count = 0
if n % 3 == 0:
    count = (n // 3 // 5) * 3 + n // 3 % 5
else:
    temp = 0
    for _ in range(6):
        temp += 1
        n -= 5
        if n < 0:
            break
        if n % 3 == 0:
            count = (n // 3 // 5) * 3 + n // 3 % 5 + temp
            break
print(count if count > 0 else -1)
