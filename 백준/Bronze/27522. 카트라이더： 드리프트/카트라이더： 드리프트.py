import heapq
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


blue_score, red_score = 0, 0
heap = []
for i in range(8):
    time, team = input().split()
    m, s, ms = time.split(":")
    heapq.heappush(heap, (m + s * 60 + ms * 60 * 100, team))

score = [10, 8, 6, 5, 4, 3, 2, 1]
for s in score:
    target = heapq.heappop(heap)[1]
    if target == "R":
        red_score += s
    else:
        blue_score += s
print("Red" if red_score > blue_score else "Blue")
