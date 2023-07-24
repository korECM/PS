import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


t = num_input()
count_str = lambda c: f'0{c}' if c < 10 else str(c)
for _ in range(t):
    h, w, n = nums_input()
    count = n // h + 1 if n % h != 0 else n // h
    floor = n % h if n % h != 0 else h
    print(f'{floor}{count_str(count)}')
