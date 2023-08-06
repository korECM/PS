import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

n, m = num_input(), num_input()
min_value = abs(n - 100)


def solve(n: int, data: set[int], acc: str):
    global min_value
    if len(acc) > 6:
        return
    if acc:
        min_value = min(min_value, abs(n - int(acc)) + len(acc))
    for datum in data:
        solve(n, data, acc + str(datum))


if m == 10:
    print(abs(n - 100))
elif m == 0:
    print(min(abs(n - 100), len(str(n))))
else:
    solve(n, set(range(0, 10)) - set(nums_input()), "")
    print(min_value)
