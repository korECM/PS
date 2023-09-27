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
                diff = abs(land[ny][nx] - land[y][x])
                new_cost = diff if diff > height else 0
                heapq.heappush(heap, (new_cost, nx, ny))

    return answer