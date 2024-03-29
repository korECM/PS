import sys
from collections import defaultdict
from math import ceil
from typing import TypeVar, Optional, Callable

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

    @staticmethod
    def print(s: str): sys.stdout.write(s)

    @staticmethod
    def println(s: str): sys.stdout.write(s + '\n')


T = TypeVar("T")


class Array:

    @staticmethod
    def init_two(a: int, b: int, init_val: T) -> list[list[T]]:
        return [[init_val for _ in range(b)] for _ in range(a)]

    @staticmethod
    def init_three(a: int, b: int, c: int, init_val: T) -> list[list[list[T]]]:
        return Array.init_two(a, b, [init_val for _ in range(c)])

    @staticmethod
    def print_two(board: list[list[any]]):
        for b in board: print(*b)


class Move:
    @staticmethod
    def generate_hv(x: int, y: int, x_range: range, y_range: range):
        """
        상하좌우 이동
        """
        g_dx, g_dy = [0, 1, -1, 0], [1, 0, 0, -1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if g_cx in x_range and g_cy in y_range:
                yield g_cx, g_cy

    @staticmethod
    def generate_hvd(x: int, y: int, x_range: range, y_range: range):
        """
        상하좌우 대각선 이동
        """
        g_dx, g_dy = [0, 1, -1, 0, -1, -1, 1, 1], [1, 0, 0, -1, -1, 1, -1, 1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if g_cx in x_range and g_cy in y_range:
                yield g_cx, g_cy


class Graph:
    _elem: dict[T, list[T]]

    def __init__(self):
        self._elem = defaultdict(list)

    def add_bidirectional_edge(self, a: T, b: T): self._elem[a].append(b); self._elem[b].append(a)

    def add_directional_edge(self, a: T, b: T): self._elem[a].append(b)

    def __getitem__(self, item: T) -> list[T]:
        return self._elem[item]


class WeightGraph:
    _elem: dict[T, list[tuple[T, int]]]

    def __init__(self):
        self._elem = defaultdict(list)

    def add_directional_edge(self, a: T, b: T, w: int): self._elem[a].append((b, w))

    def __getitem__(self, item: T) -> list[tuple[T, int]]:
        return self._elem[item]


class BinaryTreeNode:
    left: Optional['BinaryTreeNode']
    right: Optional['BinaryTreeNode']

    def __init__(self, left: Optional['BinaryTreeNode'] = None, right: Optional['BinaryTreeNode'] = None):
        self.left = left
        self.right = right

    def preorder(self, fn: Callable[['BinaryTreeNode'], None]):
        fn(self)
        if self.left:
            self.left.preorder(fn)
        if self.right:
            self.right.preorder(fn)

    def inorder(self, fn: Callable[['BinaryTreeNode'], None]):
        if self.left:
            self.left.preorder(fn)
        fn(self)
        if self.right:
            self.right.preorder(fn)

    def postorder(self, fn: Callable[['BinaryTreeNode'], None]):
        if self.left:
            self.left.preorder(fn)
        if self.right:
            self.right.preorder(fn)
        fn(self)


class TreeNode:
    child: list['TreeNode']

    def __init__(self, child: Optional[list['TreeNode']] = None):
        self.child = child if child else []


class WeightTreeNode:
    child: list[tuple['WeightTreeNode', int]]

    def __init__(self, child: Optional[list[tuple['WeightTreeNode', int]]] = None):
        if child is None:
            child = []
        self.child = child

    def __str__(self):
        return f'WeightTreeNode[${self.child}]'


def chunk(lst: list[T], size: int): return [lst[x * size:x * size + size] for x in range(0, ceil(len(lst) / size))]


V = IO.num()
tree_dict = defaultdict(WeightTreeNode)

for _ in range(V):
    a, *raw_input = IO.nums()
    for i in range(0, len(raw_input) - 1, 2):
        b, weight = raw_input[i], raw_input[i + 1]
        # if (tree_dict[a], weight) not in tree_dict[b].child:
        tree_dict[a].child.append((tree_dict[b], weight))

max_distance = 0


def solve(node: WeightTreeNode, parent: Optional[WeightTreeNode]):
    global max_distance
    if not node.child:
        return 0

    weights = []
    for child_node, weight in node.child:
        if child_node != parent:
            weights.append(solve(child_node, node) + weight)
    weights.sort(reverse=True)

    if not weights:
        return 0

    max_distance = max(max_distance, weights[0] + weights[1] if len(weights) > 1 else weights[0])
    return weights[0]


solve(tree_dict[1], None)
print(max_distance)
