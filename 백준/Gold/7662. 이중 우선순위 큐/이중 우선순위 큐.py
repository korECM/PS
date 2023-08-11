import heapq
import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

t = num_input()
for _ in range(t):
    deleted_set = set()
    count = 0
    k = num_input()
    min_heap, max_heap = [], []
    for _ in range(k):
        raw_input = input().split()
        a, b = raw_input[0], int(raw_input[1])
        if a == "I":
            heapq.heappush(min_heap, (b, count))
            heapq.heappush(max_heap, (-b, count))
            count += 1
        else:
            if b == 1:
                while max_heap and max_heap[0][1] in deleted_set:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, i = heapq.heappop(max_heap)
                    deleted_set.add(i)
            else:
                while min_heap and min_heap[0][1] in deleted_set:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, i = heapq.heappop(min_heap)
                    deleted_set.add(i)
    while min_heap and min_heap[0][1] in deleted_set:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] in deleted_set:
        heapq.heappop(max_heap)
    if not min_heap:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
