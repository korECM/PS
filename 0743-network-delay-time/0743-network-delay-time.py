import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        dist = defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            # dist는 항상 최솟값부터 설정
            # 이미 키가 존재하면 그 값은 이미 최단경로이므로 새로운 값을 버린다
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        return -1 if len(dist) != n else max(dist.values())
