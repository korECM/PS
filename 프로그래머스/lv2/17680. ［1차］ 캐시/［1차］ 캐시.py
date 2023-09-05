from collections import deque

def solution(cacheSize: int, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in map(lambda s : s.lower(), cities):
        if city not in cache:
            answer += 5
        else:
            answer += 1
            cache.remove(city)
        cache.append(city)
    return answer