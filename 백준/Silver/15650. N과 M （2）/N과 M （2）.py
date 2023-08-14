import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

def nums_input():
    return map(int, input().split())


n, m = nums_input()


def make(start: int, cnt: int, acc: list[int]):
    if start > n + 1:
        return
    if cnt == m:
        print(*acc)
        return
    make(start + 1, cnt + 1, acc + [start])
    make(start + 1, cnt, acc)


make(1, 0, [])
