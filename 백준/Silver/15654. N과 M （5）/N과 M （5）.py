import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


n, m = nums_input()
targets = sorted([*nums_input()])
visited = set()


def make(candidates: list[int], acc: list[int]):
    if len(acc) == m:
        print(*acc)
        return
    if not candidates:
        return
    for candidate in candidates:
        if candidate not in visited:
            visited.add(candidate)
            make(candidates, acc + [candidate])
            visited.remove(candidate)


make(targets, [])
