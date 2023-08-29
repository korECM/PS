from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1
                counter.subtract(task)
                counter += Counter()
            if not counter:
                break
            result += n - sub_count + 1

        return result
