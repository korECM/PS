import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


first_num = 1
mul_value = 1
add_value = 0
q = num_input()

for _ in range(q):
    raw_input = list(map(int, input().split()))
    if raw_input[0] == 3:
        print(first_num * mul_value + add_value)
    else:
        a, b = raw_input
        if a == 0:
            add_value += b
        elif a == 1:
            mul_value *= b
            add_value *= b
        else:
            first_num += b
