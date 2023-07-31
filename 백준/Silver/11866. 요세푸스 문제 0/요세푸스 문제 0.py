import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, k = nums_input()
result = []
data = [i for i in range(1, n + 1)]
start_index = 0
while data:
    index = (start_index + (k - 1)) % len(data)
    start_index = index
    result.append(str(data[index]))
    del data[index]
print(f'<{", ".join(result)}>')
