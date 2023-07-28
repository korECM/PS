import heapq
import sys
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        weight = [(sys.maxsize, K)] * n
        Q = [(0, src, K)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for n, p in graph[node]:
                    alt = price + p
                    if alt < weight[n][0] or k - 1 >= weight[n][1]:
                        weight[n] = (alt, k - 1)
                        heapq.heappush(Q, (alt, n, k - 1))

        return -1
