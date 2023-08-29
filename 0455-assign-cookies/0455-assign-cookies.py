from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        while g and s:
            if g[-1] <= s[-1]:
                result += 1
                g.pop()
                s.pop()
            else:
                s.pop()
        return result
