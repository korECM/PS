import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())


N, r, c = nums_input()
N = 2 ** N
acc = 0

while N > 2:
    N = N // 2
    location = (2 if r >= N else 0) + (1 if c >= N else 0)
    acc += (N ** 2) * location
    r %= N
    c %= N
print(acc + r * 2 + c)
