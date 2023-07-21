class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {"[": "]", "{": "}", "(": ")"}

        stack = []
        for c in s:
            if c in char_map:
                stack.append(c)
            elif not stack or char_map[stack.pop()] != c:
                return False
        return not bool(stack)
