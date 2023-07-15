class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []
        for i, h in enumerate(height):
            if not stack:
                stack.append((i, h))
                continue
            while stack and h > stack[-1][1]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1][0] - 1
                waters = min(h, stack[-1][1]) - top[1]
                volume += distance * waters
            stack.append((i, h))
        return volume