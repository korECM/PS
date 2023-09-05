import sys
from collections import deque, defaultdict
from sys import stdin as ssi

a, b = map(int, ssi.readline().split())
if a == b:
    print(0)
    print(1)
else:
    queue = deque([(a, 0)])
    min_time = sys.maxsize
    dp_map = defaultdict(lambda: sys.maxsize)
    answer_count = 0
    while queue:
        pos, time = queue.popleft()
        if pos == b:
            answer_count += 1
            if min_time == sys.maxsize:
                min_time = time
            continue
        if time == min_time:
            continue
        if time > min_time:
            break
        if pos <= 10 ** 5:
            if dp_map[pos * 2] >= time + 1:
                dp_map[pos * 2] = time + 1
                queue.append((pos * 2, time + 1))
        if pos > 0:
            if dp_map[pos - 1] >= time + 1:
                dp_map[pos - 1] = time + 1
                queue.append((pos - 1, time + 1))
        if pos <= 10 ** 5:
            if dp_map[pos + 1] >= time + 1:
                dp_map[pos + 1] = time + 1
                queue.append((pos + 1, time + 1))
    print(min_time)
    print(answer_count)
