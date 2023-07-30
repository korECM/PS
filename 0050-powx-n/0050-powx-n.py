class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x

        result = 1
        is_negative = False
        if n < 0:
            is_negative = True
            n = -n

        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n = n // 2
        return 1 / result if is_negative else result
