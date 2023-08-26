import sys
from math import ceil, sqrt
class IO:
    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def println(*args: any, sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + '\n')


is_prime = {}
is_prime[2] = True
is_prime[3] = True


def check(n: int):
    if n % 2 == 0 and n > 2:
        return False
    if n not in is_prime:
        is_prime[n] = True
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                is_prime[n] = False
                break
    return is_prime[n]


while True:
    n = IO.num()
    if n == 0:
        break
    IO.println(len([1 for i in range(n + 1, 2 * n + 1) if check(i)]))
