import heapq
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


heap = []

n = num_input()
for _ in range(n):
    op = num_input()
    if op == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, op)
