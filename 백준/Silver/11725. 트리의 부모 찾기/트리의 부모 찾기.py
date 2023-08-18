import sys
from collections import defaultdict, deque
from typing import TypeVar, Optional


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())


T = TypeVar("T")


def create_graph() -> dict[T, list[T]]:
    return defaultdict(list)


def add_bidirectional_edge(graph: dict[T, list[T]], a: T, b: T):
    graph[a].append(b)
    graph[b].append(a)

n = num_input()
graph = create_graph()
for _ in range(n - 1):
    a, b, = nums_input()
    add_bidirectional_edge(graph, a, b)

data: list[Optional[int]] = [0] * (n + 1)

queue: deque[tuple[Optional[int], int]] = deque([(None, 1)])
visited = {1}
while queue:
    parent, child = queue.popleft()
    data[child] = parent
    for n in graph[child]:
        if n not in visited:
            visited.add(n)
            queue.append((child, n))

print('\n'.join(map(str, data[2:])))
