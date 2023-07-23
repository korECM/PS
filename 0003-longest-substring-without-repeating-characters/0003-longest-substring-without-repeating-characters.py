class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = start = 0
        used = {}
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                result = max(result, index - start + 1)
            used[char] = index

        return result
