class Solution:
    def isValid(self, s: str) -> bool:
        open_char = ["[", "{", "("]
        char_map = {"[": "]", "{": "}", "(": ")"}

        stack = []
        for c in s:
            if c in open_char:
                stack.append(c)
            else:
                if not stack or char_map[stack.pop()] != c:
                    return False
        return not bool(stack)
