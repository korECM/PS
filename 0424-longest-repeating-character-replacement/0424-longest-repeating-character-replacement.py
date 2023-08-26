from collections import Counter


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == k:
            return k

        left = right = 0
        counter = Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            most_common_n = counter.most_common(1)[0][1]
            if right - left - most_common_n > k:
                counter[s[left]] -= 1
                left += 1
        return right - left
