import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

n = num_input()
n = 1000 - n
target = [500, 100, 50, 10, 5, 1]
answer = 0
for t in target:
    if n // t > 0:
        answer += n // t
        n %= t
print(answer)
