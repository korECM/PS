import sys
from collections import defaultdict
from typing import TypeVar, Optional, Callable

sys.setrecursionlimit(10**6)
MAX = sys.maxsize


class IO:
    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

class WeightTreeNode:
    child: list[tuple['WeightTreeNode', int]]

    def __init__(self, child: Optional[list[tuple['WeightTreeNode', int]]] = None):
        if child is None:
            child = []
        self.child = child


n = IO.num()
tree_dict = defaultdict(WeightTreeNode)
for _ in range(n - 1):
    p, c, w = IO.nums()
    tree_dict[p].child.append((tree_dict[c], w))

max_distance = 0


def solve(node: WeightTreeNode):
    global max_distance
    if not node.child:
        return 0

    weights = []
    for child_node, weight in node.child:
        weights.append(solve(child_node) + weight)
    weights.sort(reverse=True)

    max_distance = max(max_distance, weights[0] + weights[1] if len(weights) > 1 else weights[0])
    return weights[0]


solve(tree_dict[1])
print(max_distance)
