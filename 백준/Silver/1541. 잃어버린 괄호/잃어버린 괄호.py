import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

split_input = input().split('-')
result = 0
for i, si in enumerate(split_input):
    result += (-1 if i > 0 else 1) * sum(map(int, si.split("+")))
print(result)
