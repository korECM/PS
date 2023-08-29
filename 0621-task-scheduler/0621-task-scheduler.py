import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        time = 0
        counter = Counter(tasks)
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)

        while heap:
            more = []
            for _ in range(n + 1):
                time += 1
                if not heap:
                    if not more:
                        time -= 1
                        break
                    continue
                _, letter = heapq.heappop(heap)
                counter[letter] -= 1
                if counter[letter] > 0:
                    more.append((-counter[letter], letter))
            for item in more:
                heapq.heappush(heap, item)

        return time
