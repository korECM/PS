from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        key_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        target = [key_map[d] for d in digits]

        def dfs(index, acc="", result=[]):
            if index >= len(target):
                result.append(acc)
                return result
            for t in target[index]:
                dfs(index + 1, acc + t, result)
            return result

        return dfs(0)
