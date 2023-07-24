import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        result = [0] * k
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        for i in range(k):
            result[i] = heapq.heappop(heap)[1]
        return result
