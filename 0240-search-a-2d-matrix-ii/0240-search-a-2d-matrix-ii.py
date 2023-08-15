import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # 해당 row의 최댓값이 target보다 작을 때
            if row[-1] < target:
                continue
            # 이미 찾을 수 있는 범위를 지난 경우
            if row[0] > target:
                return False
            i = bisect.bisect_left(row, target)
            if i < len(row) and row[i] == target:
                return True
        return False
