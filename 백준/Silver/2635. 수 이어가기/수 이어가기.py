import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


def calc(a: int, b: int, acc: list[int]):
    if b < 0:
        return 1
    acc.append(a - b)
    return calc(b, a - b, acc) + 1


a = num_input()
data = {}
e = {}
for b in range(1, a + 1):
    acc = [a, b]
    data[b] = calc(a, b, acc)
    acc.pop()
    e[b] = acc
print(max(data.values()))
print(*e[max(data, key=data.get)])
