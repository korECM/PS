import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


answers = [
    [
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
    ],
    [
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
        'BWBWBWBW',
        'WBWBWBWB',
    ]
]

n, m = nums_input()
data = [""] * n
for i in range(n):
    data[i] = input()

result = sys.maxsize

for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        for answer in answers:
            count = 0
            for y in range(i, i + 8):
                for x in range(j, j + 8):
                    if data[y][x] != answer[y - i][x - j]:
                        count += 1
            result = min(result, count)
print(result)
