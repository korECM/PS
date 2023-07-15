class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in d and d[complement] > i:
                return [i, d[complement]]
