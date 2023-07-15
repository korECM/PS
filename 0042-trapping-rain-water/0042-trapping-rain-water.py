class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                _, top_height = stack.pop()
                if len(stack) == 0:
                    break
                last_index, last_height = stack[-1]
                distance = i - last_index - 1
                waters = min(h, last_height) - top_height
                volume += distance * waters
            stack.append((i, h))
        return volume