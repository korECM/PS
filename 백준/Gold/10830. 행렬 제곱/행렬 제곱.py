from sys import stdin as ssi
from sys import stdout as sso


class IO:
    @staticmethod
    def nums(): return map(int, ssi.readline().split())

    @staticmethod
    def println(*args: any, sep: str = ' '): sso.write(sep.join(map(str, args)) + '\n')


class Array:
    @staticmethod
    def print_two(board: list[list[any]]):
        for b in board: IO.println(*b)


p = 1000
N, B = IO.nums()
mat = []
for _ in range(N):
    mat.append([*IO.nums()])


def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
                c[i][j] %= p
    return c


def solve(m: list[list[int]], b: int):
    if b == 1:
        for i in range(N):
            for j in range(N):
                m[i][j] %= p
        return m
    if b == 2:
        return multiply(m, m)
    tmp = solve(m, b // 2)
    if b % 2:
        return multiply(multiply(tmp, m), tmp)
    return multiply(tmp, tmp)


Array.print_two(solve(mat, B))
