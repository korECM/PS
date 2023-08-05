from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        lo_min, hi_max = intervals[0][0], intervals[0][1]
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] <= hi_max:
                hi_max = max(hi_max, intervals[i + 1][1])
            else:
                result.append([lo_min, hi_max])
                lo_min, hi_max = intervals[i + 1][0], intervals[i + 1][1]
        return result + [[lo_min, hi_max]]
