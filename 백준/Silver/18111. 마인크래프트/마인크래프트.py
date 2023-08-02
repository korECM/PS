import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n, m, b = nums_input()
block_map = defaultdict(int)

for i in range(n):
    for e in nums_input():
        block_map[e] += 1

total_time = 0

while len(block_map) > 1:
    cur_min = min(block_map.keys())
    cur_max = max(block_map.keys())
    min_target = block_map[cur_min]
    max_target = block_map[cur_max]
    if min_target <= max_target * 2 and b >= min_target:
        b -= min_target
        block_map[cur_min + 1] += min_target
        total_time += min_target
        del block_map[cur_min]
        continue
    else:
        b += max_target
        block_map[cur_max - 1] += max_target
        del block_map[cur_max]
        total_time += 2 * max_target

print(total_time, list(block_map.keys())[0])
