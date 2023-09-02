import sys
from collections import deque
from sys import stdin as ssi
from typing import Optional, Callable

sys.setrecursionlimit(10**6)

class IO:
    @staticmethod
    def num() -> int: return int(ssi.readline())


class BinaryTreeNode:
    val: int
    left: Optional['BinaryTreeNode']
    right: Optional['BinaryTreeNode']

    def __init__(self, val: int, left: Optional['BinaryTreeNode'] = None, right: Optional['BinaryTreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def postorder(self, fn: Callable[['BinaryTreeNode'], None]):
        if self.left:
            self.left.postorder(fn)
        if self.right:
            self.right.postorder(fn)
        fn(self)


data = deque()

while True:
    try:
        data.append(IO.num())
    except:
        break


def solve(nodes: deque[int]):
    if not nodes:
        return None
    root_node = BinaryTreeNode(nodes.popleft())
    left, right = deque(), deque()
    while nodes and nodes[0] < root_node.val:
        left.append(nodes.popleft())
    right.extend(nodes)
    root_node.left = solve(left)
    root_node.right = solve(right)
    return root_node


root_node = solve(data)
root_node.postorder(lambda x: print(x.val))
