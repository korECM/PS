from collections import defaultdict
import heapq

def solution(n, costs):
    answer = 0
    
    graph = defaultdict(list)
    targets = set()
    for info in costs:
        a, b, cost = info
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        targets.add(a)
        targets.add(b)
        
    visited = set()
    heap = [(0, 0)]
    
    while heap:
        cost, i = heapq.heappop(heap)
        if i in visited:
            continue
            
        visited.add(i)
        answer += cost
        
        if len(visited) == targets:
            break
        
        for next_i, next_cost in graph[i]:
            if next_i not in visited:
                heapq.heappush(heap, (next_cost, next_i))
    
    return answer