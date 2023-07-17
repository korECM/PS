from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            init = left[i - 1] if i > 0 else 1
            left[i] = init * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            init = right[i + 1] if i < len(nums) - 1 else 1
            right[i] = init * nums[i]

        output[0] = right[1]
        output[len(nums) - 1] = left[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            output[i] = left[i - 1] * right[i + 1]

        # left   : [a    , ab   , abc , abcd, abcde]
        # right  : [abcde, bcde , cde , de  , e    ]
        # output : [bcde , acde , abde, abce, abcd ]
        return output
