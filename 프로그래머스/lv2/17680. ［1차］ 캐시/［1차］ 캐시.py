import heapq

def solution(cacheSize: int, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = {}
    for i, city in enumerate(cities):
        lo_city = city.lower()
        if lo_city not in cache:
            answer += 5
            if len(cache) == cacheSize:
                lru_key = min(cache, key=lambda x :cache[x])
                del cache[lru_key]
            cache[lo_city] = i
        else:
            answer += 1
            cache[lo_city] = i
    return answer