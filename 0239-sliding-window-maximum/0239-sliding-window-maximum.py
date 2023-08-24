from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, answer = deque(), []
        for i in range(len(nums)):
            if deq and i - deq[0] == k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            if i + 1 >= k:
                answer.append(nums[deq[0]])

        return answer
