import sys

def num_input() -> int:
    return int(input())

def nums_input():
    return map(int, input().split())

n = num_input()
data = list(nums_input())
cache = {}
for i, datum in enumerate(sorted(set(data))):
    cache[datum] = i
print(*[cache[x] for x in data])
