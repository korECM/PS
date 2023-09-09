from collections import deque

def bfs(n, node: int, computers, visited):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        for i in range(n):
            if computers[node][i] and i not in visited:
                visited.add(i)
                queue.append(i)
    return
        

def solution(n, computers):
    answer = 0
    visited = set()
    for i in range(n):
        if i not in visited:
            visited.add(i)
            bfs(n, i, computers, visited)
            answer += 1
    
    return answer