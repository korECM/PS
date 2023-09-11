from sys import stdin as ssi
from sys import stdout as sso


class IO:
    @staticmethod
    def nums(): return map(int, ssi.readline().split())

    @staticmethod
    def println(*args: any, sep: str = ' '): sso.write(sep.join(map(str, args)) + '\n')


N, M = IO.nums()


def dfs(depth, check: set[int], acc: list[int]):
    if len(check) == M:
        IO.println(*acc)
        return
    for i in range(1, N + 1):
        if i not in check:
            check.add(i)
            acc.append(i)
            dfs(depth + 1, check, acc)
            acc.pop()
            check.remove(i)


dfs(0, set(), [])
