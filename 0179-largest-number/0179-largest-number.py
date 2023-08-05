from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == {0}:
            return "0"

        def compare(a: str, b: str) -> int:
            return 1 if int(a + b) > int(b + a) else -1

        return ''.join(sorted(map(str, nums), reverse=True, key=cmp_to_key(compare)))
