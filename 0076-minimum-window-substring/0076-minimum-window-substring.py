class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        left, start, end = 0, 0, 0
        missing = len(t)
        need = Counter(t)
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            if missing == 0:
                while left < len(s) and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
        return s[start:end]