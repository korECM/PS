import heapq

def solution(n, works):
    works = [-i for i in works]
    heapq.heapify(works)
    
    while works and n > 0:
        large_work = -1 * heapq.heappop(works)
        if large_work > 1:
            heapq.heappush(works, -(large_work - 1))
        n -= 1
    return sum([i ** 2 for i in works])