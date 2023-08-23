class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry, sum = 0, 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])
            sum = carry ^ (A ^ B)
            carry = (A & B) | ((A ^ B) & carry)
            result.append(str(sum))
        if carry:
            result.append('1')

        result = int(''.join(result[::-1]), 2) & MASK
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result
