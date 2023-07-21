from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []
        for c in s:
            counter[c] -= 1
            if c in seen:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
        return "".join(stack)
