from fractions import Fraction
from sys import stdin as ssi


class IO:
    @staticmethod
    def num() -> int: return int(ssi.readline())

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


def pow(a: int, b: int, p: int):
    result, acc = 1, a
    while b:
        if b % 2 == 1:
            result *= acc
            result %= p
        b //= 2
        acc *= acc
        acc %= p
    return result


def get_reverse(n: int, p: int):
    if n == 1:
        return 1
    return pow(n, p - 2, p) % p


p = 1000000007
m = IO.num()
acc = Fraction(0, 1)
for _ in range(m):
    n, s = IO.nums()
    acc += Fraction(s, n)
s, n = acc.as_integer_ratio()
answer = (s * get_reverse(n, p)) % p
print(answer)
