from heapq import *
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list(map(lambda x: -x, nums))
        heapify(heap)
        for _ in range(k - 1):
            heappop(heap)
        return -heappop(heap)
