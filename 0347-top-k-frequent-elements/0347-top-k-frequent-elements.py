import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)
        heap = []
        result = [0] * k
        for num in nums:
            dict[num] += 1
        for key, value in dict.items():
            heapq.heappush(heap, (-value, key))
        for i in range(k):
            result[i] = heapq.heappop(heap)[1]
        return result
