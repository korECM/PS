from collections import deque
from itertools import combinations, product
import heapq

dx,dy = [1, 0, 0, -1], [0,1 , -1, 0]

def solution(land, height):
    answer = 0
    N = len(land)

    visited = set()
    heap = [(0,0,0)]
    
    while heap:
        cost, x, y = heapq.heappop(heap)
        
        if (x, y) in visited:
            continue
        visited.add((x,y))
        answer += cost
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if abs(land[ny][nx] - land[y][x]) > height:
                    heapq.heappush(heap, (abs(land[ny][nx] - land[y][x]), nx, ny))
                else:
                    heapq.heappush(heap, (0, nx, ny))

    return answer