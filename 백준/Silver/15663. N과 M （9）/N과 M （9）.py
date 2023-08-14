import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


n, m = nums_input()
targets = list(map(str, sorted([*nums_input()])))
visited = set()
visited2 = set()
results = []


def make(candidates: list[str], acc: list[str]):
    if len(acc) == m:
        check = ' '.join(acc)
        if check not in visited2:
            visited2.add(check)
            print(check)
        return
    for i, candidate in enumerate(candidates):
        if i not in visited:
            visited.add(i)
            make(candidates, acc + [candidate])
            visited.remove(i)


make(targets, [])
