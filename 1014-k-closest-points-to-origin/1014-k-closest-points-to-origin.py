import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [*map(lambda x: (x[0] ** 2 + x[1] ** 2, x), points)]
        heapq.heapify(heap)
        result = [[0, 0]] * k
        for i in range(k):
            result[i] = heapq.heappop(heap)[1]
        return result
