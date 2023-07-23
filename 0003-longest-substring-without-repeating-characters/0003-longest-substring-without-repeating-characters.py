class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for left in range(len(s)):
            right = left + 1
            while right <= len(s):
                if len(s[left:right]) != len(set(s[left:right])):
                    break
                result = max(result, right - left)
                right += 1
        return result
