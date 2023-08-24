import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        adjust = 10 ** 5
        answer = []
        heap = [(-(x + adjust), i) for i, x in enumerate(nums[:k])]
        heapq.heapify(heap)
        answer.append(-heap[0][0] - adjust)
        for i in range(1, len(nums) - k + 1):
            while heap and heap[0][1] < i: heapq.heappop(heap)
            heapq.heappush(heap, (-(nums[k + i - 1] + adjust), k + i - 1))
            answer.append(-heap[0][0] - adjust)
        return answer
