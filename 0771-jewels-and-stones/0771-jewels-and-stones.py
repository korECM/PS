from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        return sum([counter[c] for c in jewels])
